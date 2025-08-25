#!/usr/bin/env python3
"""
OPTIM-DT Framework Structure Verification Script
Validates the generated framework structure for completeness and compliance
"""

import os
import json
from pathlib import Path
from collections import defaultdict
import yaml

class FrameworkVerifier:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.errors = []
        self.warnings = []
        self.info = []
        
    def verify_structure(self):
        """Verify the complete framework structure"""
        print("🔍 OPTIM-DT Framework Structure Verification")
        print("=" * 60)
        
        # Check base directories
        self._verify_base_directories()
        
        # Check configuration
        self._verify_configuration()
        
        # Check documentation
        self._verify_documentation()
        
        # Check AMPEL structures
        self._verify_ampel_structures()
        
        # Print results
        self._print_results()
        
        return len(self.errors) == 0
    
    def _verify_base_directories(self):
        """Verify base directory structure"""
        print("\n📁 Verifying base directories...")
        
        required_dirs = [
            "00-FRAMEWORK",
            "01-ORGANIZATIONAL", 
            "02-PROCEDURAL",
            "03-TECHNICAL-AMEDEO-PELLICCIA",
            "04-INTELLIGENT",
            "05-MACHINE",
            "config",
            "docs",
            "scripts",
            "tests"
        ]
        
        for dir_name in required_dirs:
            dir_path = self.base_path / dir_name
            if dir_path.exists() and dir_path.is_dir():
                self.info.append(f"✓ {dir_name}/ exists")
            else:
                self.errors.append(f"✗ Missing directory: {dir_name}/")
    
    def _verify_configuration(self):
        """Verify configuration files"""
        print("\n⚙️  Verifying configuration...")
        
        config_file = self.base_path / "config" / "framework.yaml"
        
        if config_file.exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
                
                # Verify configuration structure
                required_keys = ["framework", "segments", "ampels", "lifecycle_phases", "total_cis"]
                for key in required_keys:
                    if key in config:
                        self.info.append(f"✓ Configuration has {key}")
                    else:
                        self.errors.append(f"✗ Missing configuration key: {key}")
                
                # Verify framework metadata
                if "framework" in config:
                    framework_info = config["framework"]
                    if "version" in framework_info:
                        self.info.append(f"✓ Framework version: {framework_info['version']}")
                    if "name" in framework_info:
                        self.info.append(f"✓ Framework name: {framework_info['name']}")
                
            except Exception as e:
                self.errors.append(f"✗ Configuration file error: {e}")
        else:
            self.errors.append("✗ Missing configuration file: config/framework.yaml")
    
    def _verify_documentation(self):
        """Verify documentation files"""
        print("\n📚 Verifying documentation...")
        
        docs_dir = self.base_path / "docs"
        
        required_docs = [
            "master_ci_catalog.md",
            "ampel_catalog.md",
            "statistics.json"
        ]
        
        for doc_file in required_docs:
            doc_path = docs_dir / doc_file
            if doc_path.exists():
                self.info.append(f"✓ Documentation: {doc_file}")
                
                # Verify content
                if doc_file == "statistics.json":
                    try:
                        with open(doc_path, 'r') as f:
                            stats = json.load(f)
                        
                        required_stats = ["ampels", "segments", "total_cis", "lifecycle_phases"]
                        for stat in required_stats:
                            if stat in stats:
                                self.info.append(f"  ✓ Statistic: {stat} = {stats[stat]}")
                            else:
                                self.warnings.append(f"  ⚠ Missing statistic: {stat}")
                    except Exception as e:
                        self.errors.append(f"✗ Statistics file error: {e}")
            else:
                self.errors.append(f"✗ Missing documentation: {doc_file}")
    
    def _verify_ampel_structures(self):
        """Verify AMPEL directory structures"""
        print("\n🏗️  Verifying AMPEL structures...")
        
        tech_dir = self.base_path / "03-TECHNICAL-AMEDEO-PELLICCIA"
        
        if not tech_dir.exists():
            self.errors.append("✗ Missing technical directory")
            return
        
        # Count AMPELs
        ampel_dirs = [d for d in tech_dir.iterdir() if d.is_dir() and d.name.startswith("AMPEL-")]
        ampel_count = len(ampel_dirs)
        
        self.info.append(f"✓ Found {ampel_count} AMPEL directories")
        
        # Verify AMPEL structure sampling
        if ampel_dirs:
            sample_ampel = ampel_dirs[0]
            self._verify_ampel_structure(sample_ampel)
        
        # Verify expected AMPEL count
        if ampel_count > 0:
            self.info.append("✓ AMPEL structures present")
        else:
            self.warnings.append("⚠ No AMPEL structures found")
    
    def _verify_ampel_structure(self, ampel_dir):
        """Verify individual AMPEL structure"""
        ampel_name = ampel_dir.name
        
        # Check for segment directories
        segment_dirs = [d for d in ampel_dir.iterdir() if d.is_dir() and "-SEGMENT" in d.name]
        
        if segment_dirs:
            self.info.append(f"  ✓ {ampel_name}: {len(segment_dirs)} segments")
            
            # Check a sample segment
            if segment_dirs:
                sample_segment = segment_dirs[0]
                ci_dirs = [d for d in sample_segment.iterdir() if d.is_dir() and d.name.startswith("CI-")]
                
                if ci_dirs:
                    self.info.append(f"    ✓ {sample_segment.name}: {len(ci_dirs)} CIs")
                    
                    # Check a sample CI
                    sample_ci = ci_dirs[0]
                    phase_dirs = [d for d in sample_ci.iterdir() if d.is_dir()]
                    
                    if phase_dirs:
                        self.info.append(f"      ✓ {sample_ci.name}: {len(phase_dirs)} phases")
                        
                        # Check for README files
                        readme_count = 0
                        for phase_dir in phase_dirs:
                            readme_path = phase_dir / "README.md"
                            if readme_path.exists():
                                readme_count += 1
                        
                        if readme_count > 0:
                            self.info.append(f"        ✓ {readme_count} README files found")
                        else:
                            self.warnings.append(f"        ⚠ No README files found")
                    else:
                        self.warnings.append(f"      ⚠ No phase directories in {sample_ci.name}")
                else:
                    self.warnings.append(f"    ⚠ No CI directories in {sample_segment.name}")
        else:
            self.warnings.append(f"  ⚠ {ampel_name}: No segment directories")
    
    def _print_results(self):
        """Print verification results"""
        print("\n" + "=" * 60)
        print("📊 VERIFICATION RESULTS")
        print("=" * 60)
        
        print(f"\n✅ INFO ({len(self.info)}):")
        for info in self.info:
            print(f"  {info}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  {warning}")
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  {error}")
        
        print("\n" + "=" * 60)
        
        if self.errors:
            print("❌ VERIFICATION FAILED")
            print(f"   {len(self.errors)} errors must be fixed")
        elif self.warnings:
            print("⚠️  VERIFICATION PASSED WITH WARNINGS")
            print(f"   {len(self.warnings)} warnings should be reviewed")
        else:
            print("✅ VERIFICATION PASSED")
            print("   Framework structure is complete and valid")
        
        print("=" * 60)


def main():
    """Main verification function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="OPTIM-DT Framework Structure Verification"
    )
    parser.add_argument(
        "--base-path",
        type=str,
        default=".",
        help="Base path of framework to verify (default: current directory)"
    )
    
    args = parser.parse_args()
    
    verifier = FrameworkVerifier(args.base_path)
    success = verifier.verify_structure()
    
    # Exit with appropriate code
    exit(0 if success else 1)


if __name__ == "__main__":
    main()