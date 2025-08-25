# OPTIM-DT Framework API Documentation

Generated: 2025-08-25 17:27:42 UTC

## Scripts

### Framework Generator

```bash
python3 scripts/generate_framework_v7.py [options]
```

**Options:**
- `--base-path PATH`: Base path for generation (default: current directory)
- `--dry-run`: Perform dry run without creating files
- `--ampel-subset AMPEL1 AMPEL2`: Generate only specific AMPELs

**Examples:**
```bash
# Generate complete framework
python3 scripts/generate_framework_v7.py

# Dry run to see what would be generated
python3 scripts/generate_framework_v7.py --dry-run

# Generate only specific AMPELs
python3 scripts/generate_framework_v7.py --ampel-subset AMPEL-01-TUW AMPEL-02-DHC
```

### Structure Verification

```bash
python3 scripts/verify_structure.py [options]
```

**Options:**
- `--base-path PATH`: Base path of framework to verify

### Documentation Generation

```bash
python3 scripts/generate_docs.py [options]
```

## Configuration

### Framework Configuration (config/framework.yaml)

The main configuration file contains:
- Framework metadata
- Segment definitions
- AMPEL count
- Lifecycle phases
- CI statistics

## Directory Structure

```
OPTIM-DT_AMEDEO-PELLICCIA/
├── 03-TECHNICAL-AMEDEO-PELLICCIA/
│   ├── AMPEL-XX-YYY/
│   │   ├── Z-SEGMENT/
│   │   │   ├── CI-Z001-NAME/
│   │   │   │   ├── 01-CONCEPT/
│   │   │   │   │   └── README.md
│   │   │   │   ├── 02-DESIGN/
│   │   │   │   │   └── README.md
│   │   │   │   └── ...
│   │   │   └── ...
│   │   └── ...
│   └── ...
├── config/
├── docs/
└── scripts/
```

