# OPTIM Framework Generator V10.0 & V8.0

Advanced framework generators for OPTIM-as-DT: AMEDEO-PELLICCIA with complete structure generation capabilities.

## **Available Generators**

| Generator | Version | AMPELs | Domains | Layers | Scale |
|-----------|---------|--------|---------|--------|-------|
| **`generate_framework_v10.py`** | **V10.0** | **35** | **5** | **5** | **Ultimate Complete** |
| `generate_framework.py` | V8.0 | 3 | 1 | 1 | Production-ready |

## **V10.0 ULTIMATE COMPLETE Features**

- ✅ **5 OPTIM Layers**: O-P-T-I-M (Organizational, Procedural, Technical, Intelligent, Machine)
- ✅ **5 Domains**: AIR (35 AMPELs), SPACE (10), GROUND (10), DEFENSE (10), CROSS (10)
- ✅ **35 Complete AMPELs**: All aircraft morphologies from TRL 2-9
- ✅ **15 AMEDEO-PELLICCIA Segments**: Complete technical breakdown
- ✅ **Constituent Assemblies (CAs)**: Per segment with variable counts
- ✅ **Configuration Items (CIs)**: Per CA with variable counts  
- ✅ **11 Lifecycle Phases**: Per CI (Requirements to Sustainment-Recycle)
- ✅ **Self-contained**: No external data dependencies
- ✅ **Massive scale**: 427K+ files, 223K+ directories
- ✅ **Dry-run capable**: Test without file creation

## **V8.0 Production Features**

- ✅ **Data externalized** to YAML files  
- ✅ **Proper error handling** throughout  
- ✅ **Comprehensive validation** with reports  
- ✅ **Professional logging** instead of prints  
- ✅ **CLI arguments** for flexibility  
- ✅ **Dry-run mode** for testing  
- ✅ **Clean code structure** with separation of concerns  
- ✅ **Type hints** for better IDE support  
- ✅ **Production-ready** error recovery  

## **Installation**

```bash
pip install -r requirements.txt
```

## **Usage Examples**

### **V10.0 Ultimate Complete Generation**

```bash
# Generate complete V10.0 framework (WARNING: 427K+ files!)
python generate_framework_v10.py

# Dry run to see structure without creating files
python generate_framework_v10.py --dry

# Custom output directory
python generate_framework_v10.py --base /path/to/output
```

### **V8.0 Production Generation**

```bash
# Basic generation
python generate_framework.py

# Dry run with validation
python generate_framework.py --dry-run --verbose

# Validate data only
python generate_framework.py --validate-only

# Generate subset for testing
python generate_framework.py --max-ampels 5 --output-dir test-output

# Full production run
python generate_framework.py --output-dir /path/to/output --data-dir /path/to/data
```

## **Performance Comparison**

| Metric | V10.0 | V8.0 |
|--------|-------|------|
| **Generation Time** | ~10-15 minutes | ~5 seconds |
| **Files Created** | 427,135 | ~158 |
| **Directories** | 223,308 | ~172 |
| **Disk Space** | ~200GB | ~50MB |
| **AMPELs** | 75 (35×5 domains) | 3 |
| **Memory Usage** | ~2GB | ~50MB |

## **V10.0 Architecture Generated**

```
OPTIM-COMPLETE-V10/
├── O-ORGANIZATIONAL/          # Enterprise governance
│   ├── 01-governance/
│   ├── 02-strategy/
│   └── ... (8 components)
├── P-PROCEDURAL/              # Process management  
│   ├── 01-lifecycle-management/
│   │   ├── 01-Requirements/
│   │   ├── 02-Design/
│   │   └── ... (11 phases each)
│   └── ... (8 components)
├── T-TECHNICAL/               # Technical implementation
│   └── AMEDEO-PELLICCIA/
│       ├── AIR/               # 35 AMPELs
│       │   ├── AMPEL-01-TUW/
│       │   │   ├── A-ARCHITECTURE/
│       │   │   │   ├── CA-A-001/
│       │   │   │   │   ├── CI-CA-A-001-001/
│       │   │   │   │   │   ├── 01-Requirements/
│       │   │   │   │   │   └── ... (11 phases)
│       │   │   │   │   └── ... (8 CIs)
│       │   │   │   └── ... (5 CAs)
│       │   │   └── ... (15 segments)
│       │   └── ... (35 AMPELs)
│       ├── SPACE/             # 10 AMPELs
│       ├── GROUND/            # 10 AMPELs  
│       ├── DEFENSE/           # 10 AMPELs
│       └── CROSS/             # 10 AMPELs
├── I-INTELLIGENT/             # AI/ML systems
│   ├── 01-machine-learning/
│   └── ... (8 components)
└── M-MACHINE/                 # Digital twin
    ├── 01-digital-twin-core/
    └── ... (8 components)
```

## **V8.0 Directory Structure (External Data)**

```
OPTIM-Framework-Generator/
├── generate_framework_v10.py   # V10.0 Ultimate complete generator
├── generate_framework.py       # V8.0 Production generator  
├── requirements.txt            # Dependencies
├── config/
│   ├── settings.yaml          # Framework generation settings
│   └── validation_rules.yaml  # Data validation rules
└── data/
    ├── master_ci_catalog/
    │   ├── architecture.yaml   # A-ARCHITECTURE CIs
    │   ├── mechanical.yaml     # M-MECHANICAL CIs
    │   ├── environmental.yaml # E-ENVIRONMENTAL CIs
    │   ├── propulsion.yaml    # P-PROPULSION CIs
    │   ├── systems.yaml       # S-SYSTEMS CIs
    │   ├── fuselage.yaml      # F-FUSELAGE CIs
    │   ├── wing.yaml          # W-WING CIs
    │   └── avionics.yaml      # V-AVIONICS CIs
    └── ampel_applicability/
        ├── ampel_01_tuw.yaml   # Tube-and-Wing
        ├── ampel_02_canard.yaml # Canard
        └── ampel_03_bwb.yaml   # Blended Wing Body
```

## **V8.0 Command Line Options**

- `--output-dir`: Output directory for the generated framework (default: OPTIM-FRAMEWORK)
- `--data-dir`: Directory containing data files (default: data)
- `--dry-run`: Simulate generation without creating files
- `--max-ampels`: Maximum number of AMPELs to generate (for testing)
- `--validate-only`: Only validate data without generating framework
- `--verbose`: Enable verbose logging

## **V10.0 Command Line Options**

- `--base`: Base directory for output (default: OPTIM-COMPLETE-V10)
- `--dry`: Dry run mode - simulate without creating files

## **V8.0 Generated Structure**

Each AMPEL directory contains:
- **README.md**: Description and applicability matrix
- **config.yaml**: Configuration data
- **Segment directories** with applicable CIs
  - Each CI directory contains a README.md with CI details

### **Sample V8.0 Output**

```
OPTIM-FRAMEWORK/
├── README.md
├── metadata.yaml
├── AMPEL-01-TUW/
│   ├── README.md
│   ├── config.yaml
│   └── A-ARCHITECTURE/
│       ├── CI-A001/
│       └── CI-A002/
└── AMPEL-02-CANARD/
    ├── README.md
    ├── config.yaml
    └── segments.../
```

## **Data Validation (V8.0)**

The V8.0 framework includes comprehensive validation:
- Master catalog structure validation
- CI format validation (3-field tuples)
- AMPEL reference validation
- Cross-reference consistency checks

## **Error Handling**

- Graceful handling of missing files
- Permission error handling
- YAML parsing error recovery
- Detailed error reporting
- Statistics tracking

## **Logging**

Professional logging with:
- Configurable log levels
- Structured log format
- Debug mode for troubleshooting
- Progress tracking
- Summary statistics

## **Recommendations**

- **For Production Use**: Use V8.0 with validated external data
- **For Complete Coverage**: Use V10.0 for ultimate framework structure
- **For Testing**: Use V10.0 with `--dry` flag first
- **For Development**: Start with V8.0, upgrade to V10.0 as needed