#!/usr/bin/env python3
"""
OPTIM-as-DT V10.0 DEMONSTRATION SCRIPT
Shows the power and scale of the V10.0 ULTIMATE COMPLETE framework
"""

import subprocess
import time
from pathlib import Path

def run_v10_demo():
    """Demonstrate V10.0 capabilities"""
    print("="*80)
    print("OPTIM-as-DT V10.0 ULTIMATE COMPLETE DEMONSTRATION")
    print("="*80)
    
    print("\n🚀 FRAMEWORK SPECIFICATIONS:")
    print("   • 5 OPTIM Layers: O-P-T-I-M")
    print("   • 5 Domains: AIR-SPACE-GROUND-DEFENSE-CROSS") 
    print("   • 35 AMPELs: Complete aircraft morphologies")
    print("   • 15 AMEDEO-PELLICCIA Segments per AMPEL")
    print("   • Variable CAs per segment, Variable CIs per CA")
    print("   • 11 Lifecycle phases per CI")
    print("   • Scale: 427,135 files, 223,308 directories")
    
    print("\n📊 FRAMEWORK SCALE:")
    print("   Total AMPELs across domains: 75 (35+10+10+10+10)")
    print("   Total Segments: 1,125 (75 AMPELs × 15 segments)")
    print("   Total CAs: ~4,050")
    print("   Total CIs: ~18,150") 
    print("   Total Phases: ~199,738")
    
    print("\n🎯 DOMAIN DISTRIBUTION:")
    print("   AIR:     35 AMPELs (complete aviation coverage)")
    print("   SPACE:   10 AMPELs (spacecraft configurations)")
    print("   GROUND:  10 AMPELs (ground vehicle systems)")
    print("   DEFENSE: 10 AMPELs (military platforms)")
    print("   CROSS:   10 AMPELs (integrated systems)")
    
    print("\n⚡ RUNNING DRY-RUN DEMONSTRATION...")
    
    try:
        # Run V10.0 dry run
        start_time = time.time()
        result = subprocess.run([
            'python3', 'generate_framework_v10.py', '--dry'
        ], capture_output=True, text=True, timeout=120)
        
        end_time = time.time()
        duration = end_time - start_time
        
        if result.returncode == 0:
            print(f"✅ V10.0 DRY RUN COMPLETED in {duration:.2f} seconds")
            
            # Extract statistics from output
            lines = result.stdout.split('\n')
            stats_section = False
            for line in lines:
                if "FINAL STATISTICS:" in line:
                    stats_section = True
                    continue
                if stats_section and line.strip().startswith("✅"):
                    print(f"   {line.strip()}")
                if "STRUCTURE GENERATED:" in line:
                    break
            
            print("\n🏗️  STRUCTURE PREVIEW:")
            structure_section = False
            for line in lines:
                if "STRUCTURE GENERATED:" in line:
                    structure_section = True
                    continue
                if structure_section and line.strip():
                    print(f"   {line.strip()}")
                if structure_section and not line.strip():
                    break
                    
        else:
            print(f"❌ Error running V10.0: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("⏰ Dry run timed out (this is normal for such a large framework)")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n🔧 AVAILABLE GENERATORS:")
    print("   V10.0: python3 generate_framework_v10.py [--dry] [--base DIR]")
    print("   V8.0:  python3 generate_framework.py [OPTIONS]")
    
    print("\n⚠️  PRODUCTION NOTES:")
    print("   • V10.0 creates 200GB+ of files - use --dry first!")
    print("   • V8.0 is production-ready with external data validation")
    print("   • V10.0 is self-contained with embedded complete data")
    
    print("\n" + "="*80)
    print("DEMONSTRATION COMPLETE!")
    print("="*80)

if __name__ == "__main__":
    # Change to the OPTIM-Framework-Generator directory
    script_dir = Path(__file__).parent
    generator_dir = script_dir / "OPTIM-Framework-Generator"
    
    if generator_dir.exists():
        import os
        os.chdir(generator_dir)
        run_v10_demo()
    else:
        print("Error: OPTIM-Framework-Generator directory not found!")
        print("Please run this script from the repository root.")