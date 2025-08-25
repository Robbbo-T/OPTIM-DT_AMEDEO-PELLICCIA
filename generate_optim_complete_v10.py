#!/usr/bin/env python3
"""
OPTIM-COMPLETE-V10 Structure Generator
Creates the exact structure specified in the problem statement
"""

import os
import argparse
from pathlib import Path
from datetime import datetime

class OPTIMCompleteV10Generator:
    """
    Generator for the exact OPTIM-COMPLETE-V10 structure as specified
    """
    
    def __init__(self, base_path="OPTIM-COMPLETE-V10", dry_run=False):
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
        # O-ORGANIZATIONAL components
        self.organizational_components = [
            "01-governance",
            "02-strategy", 
            "03-portfolio-management",
            "04-risk-management",
            "05-compliance",
            "06-quality-assurance",
            "07-change-management",
            "08-stakeholder-management"
        ]
        
        # P-PROCEDURAL components
        self.procedural_components = [
            "01-lifecycle-management",
            "02-certification-procedures",
            "03-testing-procedures", 
            "04-validation-procedures",
            "05-maintenance-procedures",
            "06-operational-procedures",
            "07-safety-procedures",
            "08-quality-procedures"
        ]
        
        # 11 Lifecycle phases
        self.lifecycle_phases = [
            "01-Requirements",
            "02-Design",
            "03-Building-Prototyping",
            "04-Executables-Packages",
            "05-Verification-Validation",
            "06-Integration-Qualification",
            "07-Certification-Security",
            "08-Production-Scale",
            "09-Ops-Services",
            "10-MRO",
            "11-Sustainment-Recycle"
        ]
        
        # Organizational subdirectories
        self.org_subdirs = ["policies", "procedures", "guidelines", "templates", "reports"]
        
    def create_dir(self, path):
        """Create directory if not in dry run mode"""
        if not self.dry_run:
            Path(path).mkdir(parents=True, exist_ok=True)
        print(f"{'[DRY RUN] ' if self.dry_run else ''}Creating directory: {path}")
        
    def create_file(self, path, content=""):
        """Create file if not in dry run mode"""
        if not self.dry_run:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        print(f"{'[DRY RUN] ' if self.dry_run else ''}Creating file: {path}")
        
    def generate_root_structure(self):
        """Generate the root directory structure"""
        print("\n=== Creating Root Structure ===")
        
        # Create base directory
        self.create_dir(self.base_path)
        
        # Create root files and directories
        self.create_file(self.base_path / "README.md", self.get_readme_content())
        self.create_dir(self.base_path / ".github")
        self.create_dir(self.base_path / "00-FRAMEWORK")
        self.create_dir(self.base_path / "config")
        self.create_dir(self.base_path / "docs")
        self.create_dir(self.base_path / "scripts")
        self.create_dir(self.base_path / "tests")
        
    def generate_o_organizational(self):
        """Generate O-ORGANIZATIONAL layer"""
        print("\n=== Creating O-ORGANIZATIONAL Layer ===")
        
        o_path = self.base_path / "O-ORGANIZATIONAL"
        self.create_dir(o_path)
        
        for component in self.organizational_components:
            component_path = o_path / component
            self.create_dir(component_path)
            
            # Create README.md for component
            readme_content = f"""# {component.split('-')[1].replace('-', ' ').title()}

## Organizational Component
- Layer: ORGANIZATIONAL
- Component: {component}
- Created: {self.timestamp}

## Structure
- Policies
- Procedures
- Guidelines
- Templates
- Reports
"""
            self.create_file(component_path / "README.md", readme_content)
            
            # Create subdirectories
            for subdir in self.org_subdirs:
                subdir_path = component_path / subdir
                self.create_dir(subdir_path)
                
    def generate_p_procedural(self):
        """Generate P-PROCEDURAL layer"""
        print("\n=== Creating P-PROCEDURAL Layer ===")
        
        p_path = self.base_path / "P-PROCEDURAL"
        self.create_dir(p_path)
        
        for component in self.procedural_components:
            component_path = p_path / component
            self.create_dir(component_path)
            
            # For lifecycle-management, create phase-config.yaml and procedures.md in each phase
            if component == "01-lifecycle-management":
                for phase in self.lifecycle_phases:
                    phase_path = component_path / phase
                    self.create_dir(phase_path)
                    
                    # Create phase-config.yaml
                    config_content = f"""phase: {phase}
description: {phase.split('-')[1].replace('-', ' ')} phase
component: {component}
status: active
created: {self.timestamp}
"""
                    self.create_file(phase_path / "phase-config.yaml", config_content)
                    
                    # Create procedures.md
                    procedures_content = f"""# {phase.split('-')[1].replace('-', ' ')} Procedures

## Phase: {phase}
## Component: {component}

### Description
{phase.split('-')[1].replace('-', ' ')} phase procedures

### Procedures
1. Planning
2. Execution
3. Verification
4. Documentation
5. Approval
"""
                    self.create_file(phase_path / "procedures.md", procedures_content)
            else:
                # For other components, just create the phase directories
                for phase in self.lifecycle_phases:
                    phase_path = component_path / phase
                    self.create_dir(phase_path)
                    
    def get_readme_content(self):
        """Generate README.md content"""
        return f"""# OPTIM-COMPLETE-V10

## OPTIM Framework Complete Structure V10.0

Generated: {self.timestamp}

### Structure

This framework provides a complete organizational and procedural structure for OPTIM-based systems.

#### O-ORGANIZATIONAL Layer
Enterprise-level governance and strategic management with 8 components:
- Governance
- Strategy  
- Portfolio Management
- Risk Management
- Compliance
- Quality Assurance
- Change Management
- Stakeholder Management

#### P-PROCEDURAL Layer
Process automation and workflow management with 8 components covering 11 lifecycle phases:
- Lifecycle Management
- Certification Procedures
- Testing Procedures
- Validation Procedures
- Maintenance Procedures
- Operational Procedures
- Safety Procedures
- Quality Procedures

### Lifecycle Phases
1. Requirements
2. Design
3. Building/Prototyping
4. Executables/Packages
5. Verification/Validation
6. Integration/Qualification
7. Certification/Security
8. Production/Scale
9. Ops/Services
10. MRO
11. Sustainment/Recycle

### Framework Version
Version: 10.0 Complete
Architecture: OPTIM-COMPLETE-V10
"""

    def generate_complete_structure(self):
        """Generate the complete OPTIM-COMPLETE-V10 structure"""
        print("="*60)
        print("OPTIM-COMPLETE-V10 STRUCTURE GENERATOR")
        print("="*60)
        
        self.generate_root_structure()
        self.generate_o_organizational()
        self.generate_p_procedural()
        
        print("\n" + "="*60)
        print("GENERATION COMPLETE!")
        print("="*60)
        print(f"Base directory: {self.base_path}")
        print(f"Dry run mode: {self.dry_run}")
        
def main():
    """Main execution"""
    parser = argparse.ArgumentParser(description="OPTIM-COMPLETE-V10 Structure Generator")
    parser.add_argument("--base", default="OPTIM-COMPLETE-V10", help="Base directory name")
    parser.add_argument("--dry-run", action="store_true", help="Dry run mode - no files created")
    
    args = parser.parse_args()
    
    generator = OPTIMCompleteV10Generator(base_path=args.base, dry_run=args.dry_run)
    generator.generate_complete_structure()

if __name__ == "__main__":
    main()