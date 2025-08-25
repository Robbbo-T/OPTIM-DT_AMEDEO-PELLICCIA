#!/usr/bin/env python3
"""
OPTIM-DT Framework Documentation Generator
Generates comprehensive documentation from the framework structure
"""

import os
import json
from pathlib import Path
from datetime import datetime
import yaml

class DocumentationGenerator:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
    def generate_docs(self):
        """Generate all documentation"""
        print("📚 OPTIM-DT Framework Documentation Generator")
        print("=" * 60)
        
        # Create docs directory if it doesn't exist
        docs_dir = self.base_path / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        # Generate overview documentation
        self._generate_overview()
        
        # Generate API documentation
        self._generate_api_docs()
        
        # Generate best practices guide
        self._generate_best_practices()
        
        # Generate certification guide
        self._generate_certification_guide()
        
        # Generate training materials
        self._generate_training_materials()
        
        # Generate index
        self._generate_index()
        
        print("\n✅ Documentation generation complete!")
    
    def _generate_overview(self):
        """Generate framework overview documentation"""
        print("\n📋 Generating framework overview...")
        
        docs_dir = self.base_path / "docs"
        overview_path = docs_dir / "framework_overview.md"
        
        with open(overview_path, 'w', encoding='utf_8') as f:
            f.write("# OPTIM-DT AMEDEO-PELLICCIA Framework Overview\n\n")
            f.write(f"Generated: {self.timestamp}\n\n")
            f.write("## Introduction\n\n")
            f.write("The OPTIM-DT AMEDEO-PELLICCIA Framework is a comprehensive Digital Twin framework ")
            f.write("for aerospace systems development, certification, and lifecycle management.\n\n")
            
            f.write("## Framework Architecture\n\n")
            f.write("The framework is organized into 5 main layers:\n\n")
            f.write("1. **00-FRAMEWORK** - Core framework components\n")
            f.write("2. **01-ORGANIZATIONAL** - Enterprise governance\n")
            f.write("3. **02-PROCEDURAL** - Process management\n")
            f.write("4. **03-TECHNICAL-AMEDEO-PELLICCIA** - 43 AMPELs × 15 segments\n")
            f.write("5. **04-INTELLIGENT** - AI/ML systems\n")
            f.write("6. **05-MACHINE** - Digital Twin implementation\n\n")
            
            f.write("## AMEDEO-PELLICCIA Segments\n\n")
            f.write("The framework defines 15 technical segments:\n\n")
            
            segments = [
                ("A-ARCHITECTURE", "Airframe structure and assembly"),
                ("M-MECHANICAL", "Mechanical systems and mechanisms"),
                ("E-ENVIRONMENTAL", "Environmental control and life support"),
                ("D-DIGITAL", "Digital systems and avionics"),
                ("E2-ENERGY", "Electrical power generation and distribution"),
                ("P-PROPULSION", "Propulsion systems and engines"),
                ("N-NAVIGATION", "Navigation and guidance systems"),
                ("C-COMMUNICATION", "Communication systems"),
                ("L-LANDING", "Landing and ground handling systems"),
                ("F-FUEL", "Fuel systems and management"),
                ("H-HYDRAULIC", "Hydraulic power systems"),
                ("P2-PNEUMATIC", "Pneumatic systems"),
                ("S-STRUCTURAL", "Structural analysis and testing"),
                ("I-INTEGRATION", "Systems integration"),
                ("T-TESTING", "Testing and validation")
            ]
            
            for segment_id, description in segments:
                f.write(f"- **{segment_id}**: {description}\n")
            
            f.write("\n## AMPEL Aircraft Morphologies\n\n")
            f.write("The framework supports 43 aircraft morphologies (AMPELs) across TRL 2-9:\n\n")
            f.write("- **TRL 9 - Operational**: 15 AMPELs (production aircraft)\n")
            f.write("- **TRL 8-7 - Flight Demonstrated**: 8 AMPELs (tested concepts)\n")
            f.write("- **TRL 6-5 - Prototype**: 8 AMPELs (prototype stage)\n")
            f.write("- **TRL 4-3 - Research**: 9 AMPELs (research concepts)\n")
            f.write("- **TRL 2 - Historical**: 3 AMPELs (historical concepts)\n\n")
            
            f.write("## Lifecycle Phases\n\n")
            f.write("Each Configuration Item (CI) follows 11 canonical lifecycle phases:\n\n")
            
            phases = [
                "01-CONCEPT", "02-DESIGN", "03-DEVELOPMENT", "04-MANUFACTURING",
                "05-TESTING", "06-CERTIFICATION", "07-PRODUCTION", "08-OPERATION",
                "09-MAINTENANCE", "10-UPGRADE", "11-DISPOSAL"
            ]
            
            for i, phase in enumerate(phases, 1):
                f.write(f"{i:2d}. **{phase}**\n")
            
            f.write("\n## Usage\n\n")
            f.write("See the [API Documentation](api/README.md) for detailed usage instructions.\n\n")
        
        print("  ✓ Framework overview")
    
    def _generate_api_docs(self):
        """Generate API documentation"""
        print("\n🔧 Generating API documentation...")
        
        api_dir = self.base_path / "docs" / "api"
        api_dir.mkdir(exist_ok=True)
        
        api_readme = api_dir / "README.md"
        
        with open(api_readme, 'w', encoding='utf_8') as f:
            f.write("# OPTIM-DT Framework API Documentation\n\n")
            f.write(f"Generated: {self.timestamp}\n\n")
            
            f.write("## Scripts\n\n")
            f.write("### Framework Generator\n\n")
            f.write("```bash\n")
            f.write("python3 scripts/generate_framework_v7.py [options]\n")
            f.write("```\n\n")
            f.write("**Options:**\n")
            f.write("- `--base-path PATH`: Base path for generation (default: current directory)\n")
            f.write("- `--dry-run`: Perform dry run without creating files\n")
            f.write("- `--ampel-subset AMPEL1 AMPEL2`: Generate only specific AMPELs\n\n")
            
            f.write("**Examples:**\n")
            f.write("```bash\n")
            f.write("# Generate complete framework\n")
            f.write("python3 scripts/generate_framework_v7.py\n\n")
            f.write("# Dry run to see what would be generated\n")
            f.write("python3 scripts/generate_framework_v7.py --dry-run\n\n")
            f.write("# Generate only specific AMPELs\n")
            f.write("python3 scripts/generate_framework_v7.py --ampel-subset AMPEL-01-TUW AMPEL-02-DHC\n")
            f.write("```\n\n")
            
            f.write("### Structure Verification\n\n")
            f.write("```bash\n")
            f.write("python3 scripts/verify_structure.py [options]\n")
            f.write("```\n\n")
            f.write("**Options:**\n")
            f.write("- `--base-path PATH`: Base path of framework to verify\n\n")
            
            f.write("### Documentation Generation\n\n")
            f.write("```bash\n")
            f.write("python3 scripts/generate_docs.py [options]\n")
            f.write("```\n\n")
            
            f.write("## Configuration\n\n")
            f.write("### Framework Configuration (config/framework.yaml)\n\n")
            f.write("The main configuration file contains:\n")
            f.write("- Framework metadata\n")
            f.write("- Segment definitions\n")
            f.write("- AMPEL count\n")
            f.write("- Lifecycle phases\n")
            f.write("- CI statistics\n\n")
            
            f.write("## Directory Structure\n\n")
            f.write("```\n")
            f.write("OPTIM-DT_AMEDEO-PELLICCIA/\n")
            f.write("├── 03-TECHNICAL-AMEDEO-PELLICCIA/\n")
            f.write("│   ├── AMPEL-XX-YYY/\n")
            f.write("│   │   ├── Z-SEGMENT/\n")
            f.write("│   │   │   ├── CI-Z001-NAME/\n")
            f.write("│   │   │   │   ├── 01-CONCEPT/\n")
            f.write("│   │   │   │   │   └── README.md\n")
            f.write("│   │   │   │   ├── 02-DESIGN/\n")
            f.write("│   │   │   │   │   └── README.md\n")
            f.write("│   │   │   │   └── ...\n")
            f.write("│   │   │   └── ...\n")
            f.write("│   │   └── ...\n")
            f.write("│   └── ...\n")
            f.write("├── config/\n")
            f.write("├── docs/\n")
            f.write("└── scripts/\n")
            f.write("```\n\n")
        
        print("  ✓ API documentation")
    
    def _generate_best_practices(self):
        """Generate best practices guide"""
        print("\n📋 Generating best practices guide...")
        
        docs_dir = self.base_path / "docs"
        bp_path = docs_dir / "best_practices.md"
        
        with open(bp_path, 'w') as f:
            f.write("# OPTIM-DT Framework Best Practices\n\n")
            f.write(f"Generated: {self.timestamp}\n\n")
            
            f.write("## Development Practices\n\n")
            f.write("### 1. Framework Generation\n\n")
            f.write("- Always perform a dry run first to validate the structure\n")
            f.write("- Use AMPEL subsets during development to reduce generation time\n")
            f.write("- Verify the structure after generation\n")
            f.write("- Keep the generated structure under version control\n\n")
            
            f.write("### 2. CI/CD Integration\n\n")
            f.write("- Automate framework verification in CI/CD pipelines\n")
            f.write("- Use the verification script to ensure structure integrity\n")
            f.write("- Generate documentation automatically\n")
            f.write("- Validate configuration files\n\n")
            
            f.write("### 3. Configuration Management\n\n")
            f.write("- Keep configuration files synchronized\n")
            f.write("- Use semantic versioning for framework releases\n")
            f.write("- Document configuration changes\n")
            f.write("- Validate YAML configuration syntax\n\n")
            
            f.write("## AMPEL Development\n\n")
            f.write("### 1. AMPEL Selection\n\n")
            f.write("- Choose AMPELs based on TRL requirements\n")
            f.write("- Consider certification requirements\n")
            f.write("- Validate AMPEL-CI applicability matrix\n")
            f.write("- Document AMPEL-specific requirements\n\n")
            
            f.write("### 2. CI Development\n\n")
            f.write("- Follow the 11 lifecycle phases consistently\n")
            f.write("- Maintain traceability across phases\n")
            f.write("- Document dependencies between CIs\n")
            f.write("- Use standard naming conventions\n\n")
            
            f.write("## Quality Assurance\n\n")
            f.write("### 1. Testing\n\n")
            f.write("- Test framework generation regularly\n")
            f.write("- Validate generated structure completeness\n")
            f.write("- Check documentation accuracy\n")
            f.write("- Verify configuration consistency\n\n")
            
            f.write("### 2. Documentation\n\n")
            f.write("- Keep documentation up to date\n")
            f.write("- Generate documentation automatically\n")
            f.write("- Review documentation for accuracy\n")
            f.write("- Maintain change logs\n\n")
        
        print("  ✓ Best practices guide")
    
    def _generate_certification_guide(self):
        """Generate certification compliance guide"""
        print("\n📜 Generating certification guide...")
        
        docs_dir = self.base_path / "docs"
        cert_path = docs_dir / "certification.md"
        
        with open(cert_path, 'w') as f:
            f.write("# OPTIM-DT Framework Certification Guide\n\n")
            f.write(f"Generated: {self.timestamp}\n\n")
            
            f.write("## Regulatory Compliance\n\n")
            f.write("The OPTIM-DT framework is designed to support compliance with:\n\n")
            f.write("- **FAR Part 25** (US Transport Category Aircraft)\n")
            f.write("- **CS-25** (European Transport Category Aircraft)\n")
            f.write("- **ARP4754A** (Guidelines for Development of Civil Aircraft and Systems)\n")
            f.write("- **ARP4761** (Safety Assessment Process)\n")
            f.write("- **DO-178C** (Software Considerations in Airborne Systems)\n")
            f.write("- **DO-254** (Design Assurance Guidance for Airborne Electronic Hardware)\n\n")
            
            f.write("## Framework Compliance Features\n\n")
            f.write("### 1. Structured Development\n\n")
            f.write("- 11 canonical lifecycle phases align with certification requirements\n")
            f.write("- Traceability across all development phases\n")
            f.write("- Configuration management support\n")
            f.write("- Change control documentation\n\n")
            
            f.write("### 2. Systems Engineering\n\n")
            f.write("- Hierarchical breakdown structure (AMPEL → Segment → CA → CI)\n")
            f.write("- Requirements allocation and verification\n")
            f.write("- Interface management\n")
            f.write("- Verification and validation planning\n\n")
            
            f.write("### 3. Safety Assessment\n\n")
            f.write("- Systematic hazard analysis support\n")
            f.write("- Failure mode identification\n")
            f.write("- Common cause analysis\n")
            f.write("- Certification by analysis framework\n\n")
            
            f.write("## Certification Artifacts\n\n")
            f.write("The framework supports generation of key certification artifacts:\n\n")
            f.write("- **Requirements Documents** - Generated from CI specifications\n")
            f.write("- **Design Documents** - Structured by segment and CI\n")
            f.write("- **Verification Plans** - Aligned with lifecycle phases\n")
            f.write("- **Configuration Lists** - Complete CI traceability\n")
            f.write("- **Safety Assessment** - Hazard analysis documentation\n\n")
            
            f.write("## Digital Twin Certification\n\n")
            f.write("### 1. Model Validation\n\n")
            f.write("- Physics-based model verification\n")
            f.write("- Simulation accuracy assessment\n")
            f.write("- Real-world correlation validation\n")
            f.write("- Uncertainty quantification\n\n")
            
            f.write("### 2. Software Qualification\n\n")
            f.write("- DO-178C compliance for digital twin software\n")
            f.write("- Design assurance level (DAL) assignment\n")
            f.write("- Software life cycle data\n")
            f.write("- Configuration management\n\n")
        
        print("  ✓ Certification guide")
    
    def _generate_training_materials(self):
        """Generate training materials"""
        print("\n🎓 Generating training materials...")
        
        training_dir = self.base_path / "docs" / "training"
        training_dir.mkdir(exist_ok=True)
        
        # Training overview
        overview_path = training_dir / "README.md"
        
        with open(overview_path, 'w') as f:
            f.write("# OPTIM-DT Framework Training Materials\n\n")
            f.write(f"Generated: {self.timestamp}\n\n")
            
            f.write("## Training Modules\n\n")
            f.write("### Module 1: Framework Introduction\n")
            f.write("- Framework overview and architecture\n")
            f.write("- OPTIM layers and their purposes\n")
            f.write("- AMEDEO-PELLICCIA segments\n")
            f.write("- Digital Twin concepts\n\n")
            
            f.write("### Module 2: AMPEL Morphologies\n")
            f.write("- Aircraft morphology classification\n")
            f.write("- TRL-based organization\n")
            f.write("- AMPEL selection criteria\n")
            f.write("- Real-world examples\n\n")
            
            f.write("### Module 3: Framework Usage\n")
            f.write("- Framework generation\n")
            f.write("- Structure verification\n")
            f.write("- Configuration management\n")
            f.write("- Best practices\n\n")
            
            f.write("### Module 4: Certification Compliance\n")
            f.write("- Regulatory requirements\n")
            f.write("- Certification artifacts\n")
            f.write("- Digital Twin qualification\n")
            f.write("- Safety assessment\n\n")
            
            f.write("## Getting Started\n\n")
            f.write("1. **Prerequisites**: Basic knowledge of aircraft systems and software development\n")
            f.write("2. **Environment Setup**: Python 3.8+, Git, Text editor\n")
            f.write("3. **Hands-on Exercises**: Practice with framework generation\n")
            f.write("4. **Certification Project**: Apply framework to real aircraft system\n\n")
        
        print("  ✓ Training materials")
    
    def _generate_index(self):
        """Generate documentation index"""
        print("\n📋 Generating documentation index...")
        
        docs_dir = self.base_path / "docs"
        index_path = docs_dir / "README.md"
        
        with open(index_path, 'w') as f:
            f.write("# OPTIM-DT Framework Documentation\n\n")
            f.write(f"Generated: {self.timestamp}\n\n")
            
            f.write("## Documentation Index\n\n")
            f.write("### Core Documentation\n")
            f.write("- [Framework Overview](framework_overview.md) - Complete framework introduction\n")
            f.write("- [Master CI Catalog](master_ci_catalog.md) - Complete CI reference\n")
            f.write("- [AMPEL Catalog](ampel_catalog.md) - Aircraft morphology reference\n")
            f.write("- [Statistics](statistics.json) - Framework statistics\n\n")
            
            f.write("### User Guides\n")
            f.write("- [API Documentation](api/README.md) - Scripts and usage\n")
            f.write("- [Best Practices](best_practices.md) - Development guidelines\n")
            f.write("- [Certification Guide](certification.md) - Compliance information\n\n")
            
            f.write("### Training\n")
            f.write("- [Training Materials](training/README.md) - Learning resources\n\n")
            
            f.write("### Configuration\n")
            f.write("- [Framework Configuration](../config/framework.yaml) - Main configuration\n\n")
            
            f.write("## Quick Start\n\n")
            f.write("1. **Generate Framework**: `python3 scripts/generate_framework_v7.py --dry-run`\n")
            f.write("2. **Verify Structure**: `python3 scripts/verify_structure.py`\n")
            f.write("3. **Read Documentation**: Start with [Framework Overview](framework_overview.md)\n\n")
        
        print("  ✓ Documentation index")


def main():
    """Main documentation generation function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="OPTIM-DT Framework Documentation Generator"
    )
    parser.add_argument(
        "--base-path",
        type=str,
        default=".",
        help="Base path of framework (default: current directory)"
    )
    
    args = parser.parse_args()
    
    generator = DocumentationGenerator(args.base_path)
    generator.generate_docs()


if __name__ == "__main__":
    main()