#!/usr/bin/env python3
"""
Generate AMPEL-01-TUW Complete Example Structure
Creates the complete structure shown in the problem statement as an example.
"""

import os
import sys
from pathlib import Path

# Add the OPTIM-Framework-Generator to the path
script_dir = Path(__file__).parent
sys.path.append(str(script_dir / 'OPTIM-Framework-Generator'))

from generate_framework_v10 import OPTIMUltimateFramework

def generate_ampel_01_example(base_path="AMPEL-01-TUW-EXAMPLE"):
    """Generate just the AMPEL-01-TUW complete example structure"""
    
    print("="*80)
    print("OPTIM-DT AMPEL-01-TUW COMPLETE EXAMPLE GENERATOR")
    print("="*80)
    
    generator = OPTIMUltimateFramework(base_path=base_path, dry=False)
    
    # Create base structure
    base = Path(base_path)
    generator.create_dir(base)
    
    # Create just T-TECHNICAL/AMEDEO-PELLICCIA/AIR/AMPEL-01-TUW structure
    t_path = generator.create_dir(base / "T-TECHNICAL")
    amedeo_path = generator.create_dir(t_path / "AMEDEO-PELLICCIA")
    air_path = generator.create_dir(amedeo_path / "AIR")
    
    # Generate README for AIR domain
    generator.create_file(air_path / "README.md", """# AIR Domain

## Description
Aviation and aerospace systems

## AMPELs
This domain contains the complete AMPEL-01-TUW example structure showing:
- Complete CA/CI hierarchical breakdown
- All 15 AMEDEO-PELLICCIA segments
- All 11 lifecycle phases per CI

## Structure
- **AMPELs**: 35 (complete aviation coverage)
- **Example**: AMPEL-01-TUW [COMPLETE EXAMPLE STRUCTURE]
""")
    
    # Generate the complete AMPEL-01-TUW structure
    ampel_path = air_path / "AMPEL-01-TUW"
    generator.generate_complete_ampel(
        ampel_path,
        "AMPEL-01-TUW",
        "Tube-and-Wing",
        "Boeing 737, Airbus A320",
        "AIR"
    )
    
    print(f"\n✅ Generated AMPEL-01-TUW complete example in {base_path}/")
    print(f"   Files: {generator.stats['files']}")
    print(f"   Directories: {generator.stats['directories']}")
    print(f"   CAs: {generator.stats['cas']}")
    print(f"   CIs: {generator.stats['cis']}")
    print(f"   Phases: {generator.stats['phases']}")
    
    # Show key structure verification
    primary_structure = ampel_path / "A-ARCHITECTURE" / "CA-A-001-PRIMARY-STRUCTURE"
    if primary_structure.exists():
        cis = list(primary_structure.glob("CI-*"))
        print(f"\n📁 CA-A-001-PRIMARY-STRUCTURE verification:")
        print(f"   CIs: {len(cis)} (expected: 8)")
        
        if cis:
            first_ci = cis[0]
            phases = list(first_ci.glob("[0-9]*"))
            print(f"   {first_ci.name} phases: {len(phases)} (expected: 11)")
    
    print(f"\n📂 Structure created:")
    print(f"   {base_path}/T-TECHNICAL/AMEDEO-PELLICCIA/AIR/AMPEL-01-TUW/")
    print(f"   ├── A-ARCHITECTURE/")
    print(f"   │   ├── CA-A-001-PRIMARY-STRUCTURE/ (8 CIs)")
    print(f"   │   ├── CA-A-002-WING-STRUCTURE/ (10 CIs)")
    print(f"   │   ├── CA-A-003-EMPENNAGE/ (7 CIs)")
    print(f"   │   ├── CA-A-004-CONTROL-SURFACES/ (9 CIs)")
    print(f"   │   └── CA-A-005-DOORS-ACCESS/ (6 CIs)")
    print(f"   ├── M-MECHANICAL/ (4 CAs)")
    print(f"   ├── E-ENVIRONMENTAL/ (4 CAs)")
    print(f"   ├── ... (11 more segments)")
    print(f"   └── Each CI has 11 lifecycle phases")
    
    return generator.stats

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate AMPEL-01-TUW Complete Example')
    parser.add_argument('--output', default='AMPEL-01-TUW-EXAMPLE', 
                       help='Output directory (default: AMPEL-01-TUW-EXAMPLE)')
    
    args = parser.parse_args()
    
    try:
        stats = generate_ampel_01_example(args.output)
        print(f"\n🎉 Success! Generated complete AMPEL-01-TUW example structure.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)