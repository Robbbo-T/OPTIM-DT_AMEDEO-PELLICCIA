# Green Framework Generator V5.0 Usage Guide

## Overview

The OPTIM-as-DT Green Framework Generator V5.0 creates sustainable aviation digital twin platforms with comprehensive green potential scoring for 35 active AMPELs (Aircraft Morphologies Programs Exemplar List).

## Features

### Green Potential Scoring System
- **Scoring Range**: 0-100 based on 5 weighted criteria
- **Categories**: 
  - ♻️ High (≥75): Prime candidates for green technology integration
  - ♻︎ Medium (60-74): Moderate potential, specific niches  
  - ◻︎ Low (<60): Limited green potential, other priorities

### Scoring Criteria (Weighted)
1. **Decarbonization** (30%): Electric/Hydrogen/SAF potential
2. **Aerodynamic Efficiency** (25%): L/D ratio, integration benefits
3. **Electrification Potential** (20%): Mass, mission profile compatibility
4. **Operational Leverage** (15%): Infrastructure, noise, routes
5. **Certification Maturity** (10%): Regulatory readiness (inverse risk)

## Usage Examples

### Basic Generation
```bash
# Generate complete framework with green focus
python3 scripts/generate_green_framework_v5.py --base OPTIM-GREEN

# Dry run to verify configuration
python3 scripts/generate_green_framework_v5.py --dry

# Limited generation for testing
python3 scripts/generate_green_framework_v5.py --max-segments 3 --top-n 5
```

### Advanced Options
```bash
# Custom configuration
python3 scripts/generate_green_framework_v5.py \
  --base /path/to/output \
  --max-segments 10 \
  --cas-per-segment 3 \
  --cis-per-ca 3 \
  --top-n 20

# Multiple domains (future)
python3 scripts/generate_green_framework_v5.py \
  --domains AIR SPACE \
  --base OPTIM-MULTI
```

## Output Structure

```
OPTIM-GREEN/
├── O-ORGANIZATIONAL/           # Sustainability governance
├── P-PROCEDURAL/              # Green certification processes  
├── T-TECHNICAL/               # AMEDEO-PELLICCIA with green scoring
│   └── AMEDEO-PELLICCIA/
│       └── AIR/
│           ├── AMPEL-01-DP/   # Top green potential AMPELs
│           ├── GREEN-REGISTRY/ # YAML/JSON registries
│           └── ...
├── I-INTELLIGENT/             # Emissions optimization AI
├── M-MACHINE/                 # Carbon footprint digital twin
└── docs/
    └── GREEN-POTENTIAL-ASSESSMENT.md
```

## Green AMPELs Distribution

- **8 High Potential**: Distributed Propulsion, BWB, TBW, Hydrogen variants
- **16 Medium Potential**: STOL, Tiltrotor, Research concepts  
- **11 Lower Potential**: Military, supersonic, specialized platforms

## Technology Roadmap

### 2025-2027: Foundation
- SAF deployment at scale
- Retrofit programs for existing fleets
- Electric trainer certification

### 2027-2030: Transition  
- Hybrid-electric regional aircraft
- Urban air mobility deployment
- Advanced aerodynamic configurations

### 2030-2035: Transformation
- Hydrogen-powered commercial aviation
- Fully electric short-haul
- Autonomous green operations

## Configuration

Edit `config/framework.yaml` to customize:
- Domain selection
- AMPEL subset and limits
- Green scoring thresholds
- Output formats

## Requirements

- Python 3.8+
- PyYAML for YAML generation
- 1-10GB disk space (depending on scope)