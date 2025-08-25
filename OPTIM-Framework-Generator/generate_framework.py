#!/usr/bin/env python3
"""
OPTIM-as-DT: AMEDEO-PELLICCIA Framework Generator V8.0
Production-ready version with external data management, validation, and error handling.
"""

import argparse
import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import yaml

# Configure logging
def setup_logging(verbose: bool = False) -> None:
    """Configure logging with appropriate level and format."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

class DataLoader:
    """Handles loading and validation of external data files."""
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def load_master_catalog(self) -> Dict:
        """Load the master CI catalog from segment files."""
        catalog_dir = self.data_dir / "master_ci_catalog"
        if not catalog_dir.exists():
            raise FileNotFoundError(f"Master catalog directory not found: {catalog_dir}")
        
        master_catalog = {}
        segment_files = list(catalog_dir.glob("*.yaml"))
        
        if not segment_files:
            raise FileNotFoundError(f"No YAML files found in {catalog_dir}")
        
        for segment_file in segment_files:
            try:
                with segment_file.open('r', encoding='utf-8') as f:
                    segment_data = yaml.safe_load(f)
                    if segment_data:
                        master_catalog.update(segment_data)
                        self.logger.debug(f"Loaded segment: {segment_file.stem}")
            except yaml.YAMLError as e:
                self.logger.error(f"Error parsing {segment_file}: {e}")
                raise
            except Exception as e:
                self.logger.error(f"Error loading {segment_file}: {e}")
                raise
        
        self.logger.info(f"Loaded {len(master_catalog)} segments from master catalog")
        return master_catalog
    
    def load_ampel_applicability(self) -> Dict:
        """Load AMPEL applicability matrices."""
        ampel_dir = self.data_dir / "ampel_applicability"
        if not ampel_dir.exists():
            raise FileNotFoundError(f"AMPEL directory not found: {ampel_dir}")
        
        ampel_data = {}
        ampel_files = list(ampel_dir.glob("*.yaml"))
        
        if not ampel_files:
            raise FileNotFoundError(f"No YAML files found in {ampel_dir}")
        
        for ampel_file in ampel_files:
            try:
                with ampel_file.open('r', encoding='utf-8') as f:
                    ampel_config = yaml.safe_load(f)
                    if ampel_config:
                        ampel_data.update(ampel_config)
                        self.logger.debug(f"Loaded AMPEL: {ampel_file.stem}")
            except yaml.YAMLError as e:
                self.logger.error(f"Error parsing {ampel_file}: {e}")
                raise
            except Exception as e:
                self.logger.error(f"Error loading {ampel_file}: {e}")
                raise
        
        self.logger.info(f"Loaded {len(ampel_data)} AMPEL configurations")
        return ampel_data

class DataValidator:
    """Validates data integrity and consistency."""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.errors = []
        self.warnings = []
    
    def validate_catalog_structure(self, catalog: Dict) -> bool:
        """Validate master catalog structure."""
        required_fields = ['description', 'cis']
        
        for segment_key, segment_data in catalog.items():
            if not isinstance(segment_data, dict):
                self.errors.append(f"Segment {segment_key} is not a dictionary")
                continue
                
            for field in required_fields:
                if field not in segment_data:
                    self.errors.append(f"Segment {segment_key} missing required field: {field}")
            
            if 'cis' in segment_data:
                if not isinstance(segment_data['cis'], list):
                    self.errors.append(f"Segment {segment_key} 'cis' field is not a list")
                else:
                    for ci in segment_data['cis']:
                        if not isinstance(ci, (list, tuple)) or len(ci) != 3:
                            self.warnings.append(f"CI in {segment_key} has invalid format: {ci}")
        
        return len(self.errors) == 0
    
    def validate_ampel_references(self, ampel_data: Dict, catalog: Dict) -> bool:
        """Validate that all CI references in AMPELs exist in the catalog."""
        # Build set of all valid CI IDs
        valid_ci_ids = set()
        for segment_data in catalog.values():
            for ci in segment_data.get('cis', []):
                if isinstance(ci, (list, tuple)) and len(ci) >= 1:
                    valid_ci_ids.add(ci[0])
        
        # Check each AMPEL's CI references
        for ampel_id, ampel_config in ampel_data.items():
            for segment_key, ci_list in ampel_config.items():
                if segment_key in ['name', 'examples', 'description']:
                    continue
                    
                if isinstance(ci_list, list):
                    for ci_id in ci_list:
                        if ci_id not in valid_ci_ids:
                            self.warnings.append(
                                f"AMPEL {ampel_id} references non-existent CI: {ci_id}"
                            )
        
        return True  # Warnings don't fail validation
    
    def get_report(self) -> str:
        """Generate validation report."""
        report = []
        if self.errors:
            report.append(f"ERRORS ({len(self.errors)}):")
            for error in self.errors:
                report.append(f"  ❌ {error}")
        
        if self.warnings:
            report.append(f"WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                report.append(f"  ⚠️  {warning}")
        
        if not self.errors and not self.warnings:
            report.append("✅ All validations passed successfully!")
        
        return "\n".join(report)

class FrameworkGenerator:
    """Main framework generation logic."""
    
    def __init__(
        self,
        output_path: Path,
        master_catalog: Dict,
        ampel_applicability: Dict,
        dry_run: bool = False,
        max_depth: Optional[int] = None
    ):
        self.output_path = output_path
        self.master_catalog = master_catalog
        self.ampel_applicability = ampel_applicability
        self.dry_run = dry_run
        self.max_depth = max_depth
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        self.logger = logging.getLogger(self.__class__.__name__)
        
        self.stats = {
            'ampels_generated': 0,
            'segments_generated': 0,
            'cis_generated': 0,
            'files_created': 0,
            'directories_created': 0,
            'errors_encountered': 0
        }
    
    def create_directory(self, path: Path) -> bool:
        """Create a directory with error handling."""
        try:
            if not self.dry_run:
                path.mkdir(parents=True, exist_ok=True)
            self.logger.debug(f"Created directory: {path}")
            self.stats['directories_created'] += 1
            return True
        except PermissionError:
            self.logger.error(f"Permission denied creating directory: {path}")
            self.stats['errors_encountered'] += 1
            return False
        except OSError as e:
            self.logger.error(f"Error creating directory {path}: {e}")
            self.stats['errors_encountered'] += 1
            return False
    
    def write_file(self, path: Path, content: str) -> bool:
        """Write a file with error handling."""
        try:
            if not self.dry_run:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open('w', encoding='utf-8') as f:
                    f.write(content)
            self.logger.debug(f"Created file: {path}")
            self.stats['files_created'] += 1
            return True
        except PermissionError:
            self.logger.error(f"Permission denied writing file: {path}")
            self.stats['errors_encountered'] += 1
            return False
        except OSError as e:
            self.logger.error(f"Error writing file {path}: {e}")
            self.stats['errors_encountered'] += 1
            return False
    
    def write_yaml(self, path: Path, data: Dict) -> bool:
        """Write a YAML file with error handling."""
        try:
            if not self.dry_run:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open('w', encoding='utf-8') as f:
                    yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
            self.logger.debug(f"Created YAML: {path}")
            self.stats['files_created'] += 1
            return True
        except Exception as e:
            self.logger.error(f"Error writing YAML {path}: {e}")
            self.stats['errors_encountered'] += 1
            return False
    
    def generate_ampel_structure(self, ampel_id: str, ampel_config: Dict) -> None:
        """Generate structure for a single AMPEL."""
        ampel_path = self.output_path / ampel_id
        
        if not self.create_directory(ampel_path):
            return
        
        # Generate README
        readme_content = self._generate_ampel_readme(ampel_id, ampel_config)
        self.write_file(ampel_path / "README.md", readme_content)
        
        # Generate configuration
        config_data = self._generate_ampel_config(ampel_id, ampel_config)
        self.write_yaml(ampel_path / "config.yaml", config_data)
        
        # Generate applicable CIs
        ci_count = self._generate_applicable_cis(ampel_path, ampel_id, ampel_config)
        
        self.logger.info(f"Generated {ampel_id} with {ci_count} applicable CIs")
        self.stats['ampels_generated'] += 1
    
    def _generate_ampel_readme(self, ampel_id: str, ampel_config: Dict) -> str:
        """Generate README content for an AMPEL."""
        content = [
            f"# {ampel_id}: {ampel_config.get('name', 'Unknown')}",
            f"\nGenerated: {self.timestamp}",
            f"\n## Description\n{ampel_config.get('description', 'No description available')}",
            f"\n## Examples"
        ]
        
        examples = ampel_config.get('examples', [])
        if examples:
            for example in examples:
                content.append(f"- {example}")
        else:
            content.append("- No examples available")
        
        content.append("\n## Applicability Matrix\n")
        content.append("| Segment | Applicable CIs | Coverage |")
        content.append("|---------|----------------|----------|")
        
        total_applicable = 0
        for segment_key in self.master_catalog.keys():
            applicable_cis = ampel_config.get(segment_key, [])
            if applicable_cis:
                total_cis = len(self.master_catalog[segment_key].get('cis', []))
                coverage = f"{len(applicable_cis)}/{total_cis}"
                content.append(f"| {segment_key} | {len(applicable_cis)} | {coverage} |")
                total_applicable += len(applicable_cis)
        
        content.append(f"\n**Total Applicable CIs: {total_applicable}**")
        return "\n".join(content)
    
    def _generate_ampel_config(self, ampel_id: str, ampel_config: Dict) -> Dict:
        """Generate configuration data for an AMPEL."""
        return {
            'ampel_id': ampel_id,
            'name': ampel_config.get('name', 'Unknown'),
            'description': ampel_config.get('description', ''),
            'examples': ampel_config.get('examples', []),
            'generated': self.timestamp,
            'statistics': {
                'total_segments': len([k for k in ampel_config.keys() 
                                       if k not in ['name', 'examples', 'description']]),
                'total_cis': sum(len(v) for k, v in ampel_config.items() 
                                if isinstance(v, list))
            }
        }
    
    def _generate_applicable_cis(self, ampel_path: Path, ampel_id: str, 
                                 ampel_config: Dict) -> int:
        """Generate CI directories for applicable CIs."""
        ci_count = 0
        
        for segment_key, segment_data in self.master_catalog.items():
            applicable_ci_ids = ampel_config.get(segment_key, [])
            
            if not applicable_ci_ids:
                continue
            
            segment_path = ampel_path / segment_key
            if not self.create_directory(segment_path):
                continue
            
            self.stats['segments_generated'] += 1
            
            # Create only applicable CIs
            for ci_tuple in segment_data.get('cis', []):
                if len(ci_tuple) >= 3:
                    ci_id, ci_name, ci_desc = ci_tuple[0], ci_tuple[1], ci_tuple[2]
                    
                    if ci_id in applicable_ci_ids:
                        ci_path = segment_path / ci_id
                        if self.create_directory(ci_path):
                            readme = f"# {ci_id}: {ci_name}\n\n{ci_desc}\n\nApplicable to: {ampel_id}"
                            self.write_file(ci_path / "README.md", readme)
                            ci_count += 1
                            self.stats['cis_generated'] += 1
        
        return ci_count
    
    def generate_framework(self) -> None:
        """Generate the complete framework."""
        self.logger.info("="*80)
        self.logger.info("OPTIM-as-DT Framework Generator V8.0")
        self.logger.info(f"Output directory: {self.output_path}")
        self.logger.info(f"Dry run: {self.dry_run}")
        self.logger.info("="*80)
        
        # Create root directory
        if not self.create_directory(self.output_path):
            self.logger.error("Failed to create output directory. Aborting.")
            return
        
        # Generate framework documentation
        self._generate_framework_docs()
        
        # Generate each AMPEL
        ampel_count = 0
        for ampel_id, ampel_config in self.ampel_applicability.items():
            if self.max_depth and ampel_count >= self.max_depth:
                self.logger.info(f"Reached maximum depth limit ({self.max_depth})")
                break
            
            self.logger.info(f"Generating {ampel_id}...")
            self.generate_ampel_structure(ampel_id, ampel_config)
            ampel_count += 1
        
        # Print summary
        self.print_summary()
    
    def _generate_framework_docs(self) -> None:
        """Generate root-level framework documentation."""
        # Main README
        readme = [
            "# OPTIM-as-DT Framework",
            f"\nGenerated: {self.timestamp}",
            "\n## Statistics",
            f"- Total AMPELs: {len(self.ampel_applicability)}",
            f"- Total Segments: {len(self.master_catalog)}",
            "\n## Structure",
            "Each AMPEL directory contains:",
            "- README.md: Description and applicability matrix",
            "- config.yaml: Configuration data",
            "- Segment directories with applicable CIs"
        ]
        self.write_file(self.output_path / "README.md", "\n".join(readme))
        
        # Metadata
        metadata = {
            'framework': 'OPTIM-as-DT',
            'version': '8.0',
            'generated': self.timestamp,
            'statistics': {
                'total_ampels': len(self.ampel_applicability),
                'total_segments': len(self.master_catalog)
            }
        }
        self.write_yaml(self.output_path / "metadata.yaml", metadata)
    
    def print_summary(self) -> None:
        """Print generation summary."""
        self.logger.info("="*80)
        self.logger.info("GENERATION COMPLETE")
        self.logger.info("="*80)
        self.logger.info("Statistics:")
        for key, value in self.stats.items():
            self.logger.info(f"  {key}: {value}")
        
        if self.stats['errors_encountered'] > 0:
            self.logger.warning(f"⚠️  Encountered {self.stats['errors_encountered']} errors during generation")
        else:
            self.logger.info("✅ Generation completed without errors")

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="OPTIM-as-DT Framework Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('OPTIM-FRAMEWORK'),
        help='Output directory for the generated framework'
    )
    
    parser.add_argument(
        '--data-dir',
        type=Path,
        default=Path('data'),
        help='Directory containing data files'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simulate generation without creating files'
    )
    
    parser.add_argument(
        '--max-ampels',
        type=int,
        help='Maximum number of AMPELs to generate (for testing)'
    )
    
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only validate data without generating framework'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.verbose)
    logger = logging.getLogger('main')
    
    try:
        # Load data
        logger.info("Loading data files...")
        loader = DataLoader(args.data_dir)
        master_catalog = loader.load_master_catalog()
        ampel_applicability = loader.load_ampel_applicability()
        
        # Validate data
        logger.info("Validating data integrity...")
        validator = DataValidator()
        catalog_valid = validator.validate_catalog_structure(master_catalog)
        validator.validate_ampel_references(ampel_applicability, master_catalog)
        
        logger.info("\nValidation Report:")
        print(validator.get_report())
        
        if not catalog_valid:
            logger.error("Critical validation errors found. Aborting.")
            sys.exit(1)
        
        if args.validate_only:
            logger.info("Validation complete. Exiting (--validate-only mode).")
            sys.exit(0)
        
        # Generate framework
        generator = FrameworkGenerator(
            output_path=args.output_dir,
            master_catalog=master_catalog,
            ampel_applicability=ampel_applicability,
            dry_run=args.dry_run,
            max_depth=args.max_ampels
        )
        
        generator.generate_framework()
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose:
            logger.exception("Full traceback:")
        sys.exit(1)

if __name__ == "__main__":
    main()