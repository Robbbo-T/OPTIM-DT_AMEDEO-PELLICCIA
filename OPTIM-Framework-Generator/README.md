# OPTIM Framework Generator V8.0

Production-ready framework generator for OPTIM-as-DT: AMEDEO-PELLICCIA with external data management, validation, and error handling.

## Features

- ✅ **Data externalized** to YAML files  
- ✅ **Proper error handling** throughout  
- ✅ **Comprehensive validation** with reports  
- ✅ **Professional logging** instead of prints  
- ✅ **CLI arguments** for flexibility  
- ✅ **Dry-run mode** for testing  
- ✅ **Clean code structure** with separation of concerns  
- ✅ **Type hints** for better IDE support  
- ✅ **Production-ready** error recovery  

## Directory Structure

```
OPTIM-Framework-Generator/
├── generate_framework.py       # Clean, maintainable script
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

## Installation

```bash
pip install -r requirements.txt
```

## Usage Examples

### Basic generation
```bash
python generate_framework.py
```

### Dry run with validation
```bash
python generate_framework.py --dry-run --verbose
```

### Validate data only
```bash
python generate_framework.py --validate-only
```

### Generate subset for testing
```bash
python generate_framework.py --max-ampels 5 --output-dir test-output
```

### Full production run
```bash
python generate_framework.py --output-dir /path/to/output --data-dir /path/to/data
```

## Command Line Options

- `--output-dir`: Output directory for the generated framework (default: OPTIM-FRAMEWORK)
- `--data-dir`: Directory containing data files (default: data)
- `--dry-run`: Simulate generation without creating files
- `--max-ampels`: Maximum number of AMPELs to generate (for testing)
- `--validate-only`: Only validate data without generating framework
- `--verbose`: Enable verbose logging

## Generated Structure

Each AMPEL directory contains:
- **README.md**: Description and applicability matrix
- **config.yaml**: Configuration data
- **Segment directories** with applicable CIs
  - Each CI directory contains a README.md with CI details

## Sample Output

```
OPTIM-FRAMEWORK/
├── README.md
├── metadata.yaml
├── AMPEL-01-TUW/
│   ├── README.md
│   ├── config.yaml
│   ├── A-ARCHITECTURE/
│   │   ├── CI-A001/
│   │   │   └── README.md
│   │   └── CI-A002/
│   │       └── README.md
│   └── M-MECHANICAL/
│       └── CI-M001/
│           └── README.md
└── AMPEL-02-CANARD/
    ├── README.md
    ├── config.yaml
    └── ...
```

## Data Validation

The framework includes comprehensive validation:
- Master catalog structure validation
- CI format validation (3-field tuples)
- AMPEL reference validation
- Cross-reference consistency checks

## Error Handling

- Graceful handling of missing files
- Permission error handling
- YAML parsing error recovery
- Detailed error reporting
- Statistics tracking

## Logging

Professional logging with:
- Configurable log levels
- Structured log format
- Debug mode for troubleshooting
- Progress tracking
- Summary statistics