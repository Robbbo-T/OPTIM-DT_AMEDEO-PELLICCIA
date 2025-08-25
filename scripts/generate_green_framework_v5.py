#!/usr/bin/env python3
"""
OPTIM-as-DT: AMEDEO-PELLICCIA Framework Generator V5.0
Active Programs with Green Potential Scoring
35 Active AMPELs with sustainability assessment
"""

import os
import argparse
import json
from pathlib import Path
from datetime import datetime
import yaml

class OPTIMGreenFramework:
    def __init__(self, base_path=".", max_segments=15, cas_per_segment=3, cis_per_ca=3, dry=False):
        self.base_path = Path(base_path)
        self.max_segments = max_segments
        self.cas_per_segment = cas_per_segment
        self.cis_per_ca = cis_per_ca
        self.dry = dry
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
        # 35 ACTIVE AMPELs with GREEN POTENTIAL SCORING
        self.active_ampels_green = [
            # HIGH GREEN POTENTIAL (♻️) - Score ≥75
            ("01", "DP", "Distributed Propulsion", 6, "DEVELOPMENT", "X-57, Lilium, Electra", 88, "High", 
             ["electrification", "efficiency", "noise_reduction"], "Medium", "Medium", "Low"),
            ("02", "BWB", "Blended Wing Body", 6, "DEVELOPMENT", "JetZero, MAVERIC", 85, "High",
             ["efficiency", "hydrogen_volume", "low_noise"], "Low", "High", "Medium"),
            ("03", "TBW", "Truss-Braced Wing", 6, "DEVELOPMENT", "X-66A, NASA TTBW", 82, "High",
             ["efficiency", "electrification", "structure"], "Medium", "Medium", "Low"),
            ("04", "HYDROGEN-TUBE", "Hydrogen Tube Wing", 5, "DEVELOPMENT", "ZeroAvia, Airbus ZEROe", 80, "High",
             ["zero_emission", "existing_infra", "scalability"], "Low", "High", "Medium"),
            ("05", "HYDROGEN-BWB", "Hydrogen BWB", 5, "DEVELOPMENT", "Airbus ZEROe BWB", 78, "High",
             ["zero_emission", "efficiency", "volume"], "Low", "High", "High"),
            ("06", "eSTOL", "Electric STOL", 5, "DEVELOPMENT", "Electra.aero", 77, "High",
             ["electrification", "short_field", "quiet"], "Medium", "Medium", "Low"),
            ("07", "ELECTRIC-ROTARY", "Electric Rotary Wing", 8, "DEVELOPMENT", "Joby, Archer", 76, "High",
             ["zero_emission_local", "urban", "modular"], "High", "Low", "Medium"),
            ("08", "SOLAR", "Solar Powered", 7, "OPERATIONAL", "Zephyr S", 75, "High",
             ["zero_emission", "persistence", "HAPS"], "Low", "Low", "High"),
            
            # MEDIUM GREEN POTENTIAL (♻︎) - Score 60-74
            ("09", "TUW", "Tube-and-Wing", 9, "PRODUCTION", "A320neo, 737MAX, A350", 68, "Medium",
             ["SAF_ready", "retrofit_easy", "mature"], "High", "Low", "Low"),
            ("10", "ELECTRIC-FIXED", "Electric Fixed Wing", 9, "PRODUCTION", "Velis Electro", 72, "Medium",
             ["zero_emission", "training", "short_range"], "High", "Low", "Low"),
            ("11", "HYBRID-AIRSHIP", "Hybrid Airship", 7, "DEVELOPMENT", "LMH-1, LCA60T", 65, "Medium",
             ["efficiency", "cargo", "low_infra"], "Low", "Medium", "High"),
            ("12", "COMPOUND-HELI", "Compound Helicopter", 8, "DEVELOPMENT", "S-97, RACER", 63, "Medium",
             ["speed", "efficiency", "hybrid_potential"], "Medium", "Medium", "Low"),
            ("13", "TILTWING", "Tiltwing", 5, "DEVELOPMENT", "NASA concepts", 62, "Medium",
             ["efficiency", "eVTOL", "regional"], "Low", "High", "Medium"),
            ("14", "AUTOGYRO", "Autogyro", 9, "PRODUCTION", "AutoGyro, Magni", 60, "Medium",
             ["simplicity", "safety", "low_fuel"], "High", "Low", "Low"),
            
            # OPERATIONAL WITH RETROFIT POTENTIAL
            ("15", "CANARD", "Canard", 9, "PRODUCTION", "Rafale, Typhoon, P180", 64, "Medium",
             ["efficiency", "control", "military"], "Medium", "Low", "Low"),
            ("16", "STOL", "Short Take-Off and Landing", 9, "PRODUCTION", "Twin Otter, Kodiak", 70, "Medium",
             ["hybrid_ready", "remote_ops", "efficiency"], "High", "Low", "Low"),
            ("17", "AMPHIBIOUS", "Amphibious", 9, "PRODUCTION", "US-2, Icon A5", 61, "Medium",
             ["versatility", "SAR", "hybrid_potential"], "Medium", "Low", "Medium"),
            ("18", "TILTROTOR", "Tiltrotor", 9, "PRODUCTION", "V-22, V-280, AW609", 66, "Medium",
             ["speed", "versatility", "hybrid_future"], "Low", "Medium", "Low"),
            
            # LOWER GREEN POTENTIAL BUT ACTIVE
            ("19", "TAILLESS", "Tailless/Flying Wing", 9, "OPERATIONAL", "B-2, B-21", 58, "Low",
             ["stealth", "efficiency", "military"], "Low", "Low", "Low"),
            ("20", "DELTA", "Delta Wing", 9, "PRODUCTION", "Tejas Mk1A", 55, "Low",
             ["supersonic", "military", "limited_civil"], "Low", "Low", "Low"),
            ("21", "VGW", "Variable Geometry Wing", 9, "OPERATIONAL", "B-1B, Tu-160M", 52, "Low",
             ["complexity", "military", "high_fuel"], "Low", "Low", "Low"),
            ("22", "VTOL-JET", "VTOL Jet", 9, "PRODUCTION", "F-35B", 50, "Low",
             ["military", "complex", "high_fuel"], "Low", "Low", "Low"),
            ("23", "SUPERSONIC", "Supersonic", 8, "DEVELOPMENT", "Boom, X-59", 48, "Low",
             ["speed", "premium", "SAF_only"], "Low", "High", "Medium"),
            ("24", "BIPLANE", "Biplane", 9, "PRODUCTION", "Pitts, WACO", 45, "Low",
             ["niche", "aerobatic", "limited"], "Medium", "Low", "Low"),
            ("25", "TWIN-FUSELAGE", "Twin Fuselage", 9, "OPERATIONAL", "Stratolaunch", 42, "Low",
             ["special_mission", "launch", "limited"], "Low", "Low", "High"),
            
            # RESEARCH WITH GREEN POTENTIAL
            ("26", "JW", "Joined Wing", 4, "RESEARCH", "NASA SensorCraft", 71, "Medium",
             ["efficiency", "structure", "sensors"], "Low", "High", "Medium"),
            ("27", "BW", "Box Wing", 4, "RESEARCH", "PrandtlPlane", 73, "Medium",
             ["efficiency", "capacity", "stability"], "Low", "High", "Medium"),
            ("28", "MW", "Morphing Wing", 3, "RESEARCH", "NASA MADCAT", 69, "Medium",
             ["adaptive", "efficiency", "materials"], "Low", "High", "High"),
            ("29", "BLI", "Boundary Layer Ingestion", 4, "RESEARCH", "STARC-ABL", 74, "Medium",
             ["efficiency", "integration", "propulsion"], "Low", "High", "Medium"),
            ("30", "ORNITHOPTER", "Ornithopter", 3, "RESEARCH", "Festo, DelFly", 40, "Low",
             ["biomimetic", "MAV", "limited"], "Low", "High", "High"),
            ("31", "MODULAR", "Modular Reconfigurable", 3, "RESEARCH", "Clip-Air", 67, "Medium",
             ["flexibility", "utilization", "concept"], "Low", "High", "High"),
            
            # ACTIVE DEVELOPMENT
            ("32", "LIFTING-BODY", "Lifting Body", 7, "DEVELOPMENT", "Dream Chaser", 35, "Low",
             ["space", "reentry", "limited_aviation"], "Low", "Low", "High"),
            ("33", "GROUND-EFFECT", "Ground Effect Vehicle", 7, "DEVELOPMENT", "REGENT, Liberty", 62, "Medium",
             ["efficiency", "maritime", "limited_routes"], "Low", "Medium", "High"),
            ("34", "HYPERSONIC", "Hypersonic", 6, "DEVELOPMENT", "Hermeus, Talon-A", 30, "Low",
             ["speed", "military", "extreme_fuel"], "Low", "High", "High"),
            ("35", "TANDEM", "Tandem Wing", 7, "PRODUCTION", "Velocity V-Twin", 59, "Low",
             ["efficiency", "kit", "limited"], "Medium", "Low", "Low"),
        ]
        
        # Green scoring rubric
        self.green_rubric = {
            "decarbonization": 0.30,  # Electric/Hydrogen/SAF
            "aerodynamic_efficiency": 0.25,  # L/D, integration
            "electrification_potential": 0.20,  # Mass, mission, architecture
            "operational_leverage": 0.15,  # Short routes, noise, existing infra
            "certification_maturity": 0.10,  # Inverse risk
        }
        
        # 15 AMEDEO-PELLICCIA segments
        self.segments = [
            ("ARC", "ARCHITECTURE"),
            ("MEC", "MECHANICAL"),
            ("ENV", "ENVIRONMENTAL"),
            ("DIG", "DIGITAL"),
            ("ENR", "ENERGY"),
            ("OPS", "OPERATIONS"),
            ("PRO", "PROPULSION"),
            ("ELE", "ELECTRONICS"),
            ("LOG", "LOGISTICS"),
            ("LNK", "LINKS"),
            ("INT", "INTEGRATION"),
            ("CTL", "CONTROL"),
            ("CER", "CERTIFICATION"),
            ("ITL", "INTELLIGENCE"),
            ("APT", "AIRPORTS")
        ]
        
        # 11 canonical lifecycle phases
        self.phases = [
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
        
        # 5 domains
        self.domains = ["AIR", "SPACE", "DEFENSE", "GROUND", "CROSS"]
        
        # Statistics
        self.stats = {
            'ampels': 0,
            'segments': 0,
            'cas': 0,
            'cis': 0,
            'phases': 0,
            'files': 0,
            'directories': 0
        }

    def get_utcs_header(self, doc_type, identifier):
        """Generate UTCS-MI header"""
        return (f"EstándarUniversal:Documento-{doc_type}-ARP4754A-00.00-"
                f"{identifier}-0001-v1.0-OPTIM-as-DT-GeneracionHumana-AIR-"
                "AmedeoPelliccia-7f3c9a2b-Diseno→Operacion\n\n")

    def get_green_emoji(self, score):
        """Get green potential emoji based on score"""
        if score >= 75:
            return "♻️"  # High
        elif score >= 60:
            return "♻︎"  # Medium
        else:
            return "◻︎"  # Low

    def create_dir(self, path):
        """Create directory with dry-run support"""
        path = Path(path)
        if not self.dry:
            path.mkdir(parents=True, exist_ok=True)
        self.stats['directories'] += 1
        return path

    def create_file(self, path, content):
        """Create file with dry-run support"""
        if not self.dry:
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(content)
        self.stats['files'] += 1

    def create_yaml(self, path, data):
        """Create YAML file with safe dump"""
        if not self.dry:
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)
        self.stats['files'] += 1

    def create_json(self, path, data):
        """Create JSON file"""
        if not self.dry:
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        self.stats['files'] += 1

    def create_green_potential_document(self):
        """Create comprehensive green potential assessment document"""
        header = self.get_utcs_header("Assessment", "GREEN-POTENTIAL")
        
        doc_content = header + """# Green Potential Assessment for Active AMPELs
## Sustainability and Decarbonization Scoring

### Scoring Rubric (0-100)
| Criterion | Weight | Description |
|-----------|--------|-------------|
| Decarbonization | 30% | Electric/Hydrogen/SAF potential |
| Aerodynamic Efficiency | 25% | L/D ratio, integration benefits |
| Electrification Potential | 20% | Mass, mission profile compatibility |
| Operational Leverage | 15% | Infrastructure, noise, routes |
| Certification Maturity | 10% | Regulatory readiness (inverse risk) |

### Green Potential Categories
- ♻️ **High** (≥75): Prime candidates for green technology integration
- ♻︎ **Medium** (60-74): Moderate potential, specific niches
- ◻︎ **Low** (<60): Limited green potential, other priorities

---

## AMPELs Ranked by Green Potential

"""
        
        # Sort by green score
        sorted_ampels = sorted(self.active_ampels_green, key=lambda x: x[6], reverse=True)
        
        # High potential
        doc_content += "### ♻️ High Green Potential (Score ≥75)\n\n"
        for ampel in sorted_ampels:
            if ampel[6] >= 75:
                num, code, desc, trl, status, programs, score, class_, drivers, retrofit, cert, infra = ampel
                emoji = self.get_green_emoji(score)
                doc_content += f"#### {emoji} AMPEL-{num}-{code}: {desc}\n"
                doc_content += f"- **Score**: {score}/100\n"
                doc_content += f"- **TRL**: {trl} | **Status**: {status}\n"
                doc_content += f"- **Programs**: {programs}\n"
                doc_content += f"- **Key Drivers**: {', '.join(drivers)}\n"
                doc_content += f"- **Retrofit**: {retrofit} | **Cert Risk**: {cert} | **Infra Impact**: {infra}\n\n"
        
        # Medium potential
        doc_content += "### ♻︎ Medium Green Potential (Score 60-74)\n\n"
        for ampel in sorted_ampels:
            if 60 <= ampel[6] < 75:
                num, code, desc, trl, status, programs, score, class_, drivers, retrofit, cert, infra = ampel
                emoji = self.get_green_emoji(score)
                doc_content += f"#### {emoji} AMPEL-{num}-{code}: {desc}\n"
                doc_content += f"- **Score**: {score}/100\n"
                doc_content += f"- **Programs**: {programs}\n"
                doc_content += f"- **Key Drivers**: {', '.join(drivers)}\n\n"
        
        # Low potential
        doc_content += "### ◻︎ Lower Green Potential (Score <60)\n\n"
        doc_content += "| AMPEL | Score | Primary Limitation |\n"
        doc_content += "|-------|-------|-------------------|\n"
        for ampel in sorted_ampels:
            if ampel[6] < 60:
                num, code, desc, trl, status, programs, score, class_, drivers, retrofit, cert, infra = ampel
                limitation = drivers[0] if drivers else "various"
                doc_content += f"| {num}-{code} | {score} | {limitation} |\n"
        
        doc_content += f"""

---

## Implementation Roadmap

### Wave 1: Immediate Retrofits (2025-2027)
- TUW: SAF 100%, winglets, laminar flow
- STOL/Amphibious: Hybrid-electric conversions
- Electric-Fixed: Scale production

### Wave 2: New Platforms (2027-2030)
- TBW: X-66A certification
- DP: Distributed electric propulsion
- eVTOL: Urban air mobility deployment

### Wave 3: Breakthrough Technologies (2030-2035)
- BWB: Commercial hydrogen
- Hydrogen-Tube: Regional operations
- BLI: Integrated propulsion

Generated: {self.timestamp}
"""
        return doc_content

    def create_ci_structure(self, ci_path, ci_name):
        """Create Configuration Item with lifecycle phases"""
        ci_dir = self.create_dir(ci_path)
        
        # CI metadata
        self.create_yaml(ci_dir / "ci-config.yaml", {
            "ci": ci_name,
            "lifecycle_phases": self.phases,
            "created": self.timestamp,
            "status": "ACTIVE"
        })
        
        # Create lifecycle phases (limited by configuration)
        for phase in self.phases[:min(len(self.phases), 5)]:  # Limit phases in reduced mode
            phase_dir = self.create_dir(ci_dir / phase)
            self.create_file(phase_dir / "requirements.md", f"# {phase}: {ci_name}\n")
        
        self.stats['cis'] += 1
        self.stats['phases'] += min(len(self.phases), 5)

    def create_segment_structure(self, segment_path, seg_code, seg_name):
        """Create segment with limited CA/CI structure"""
        seg_dir = self.create_dir(segment_path)
        
        # Create limited CAs per segment
        for ca_idx in range(1, min(self.cas_per_segment + 1, 4)):
            ca_id = f"CA-{seg_code}{ca_idx:03d}"
            ca_name = f"{seg_name}-SUBSYSTEM-{ca_idx}"
            ca_dir = self.create_dir(seg_dir / f"{ca_id}-{ca_name}")
            
            # Create limited CIs
        for ca_idx in range(1, min(self.cas_per_segment + 1, self.MAX_CAS_PER_SEGMENT)):
            ca_id = f"CA-{seg_code}{ca_idx:03d}"
            ca_name = f"{seg_name}-SUBSYSTEM-{ca_idx}"
            ca_dir = self.create_dir(seg_dir / f"{ca_id}-{ca_name}")
            
            # Create limited CIs
            for ci_idx in range(1, min(self.cis_per_ca + 1, self.MAX_CIS_PER_CA)):
                ci_name = f"CI-{seg_code}{ca_idx:03d}-{ci_idx:03d}"
                self.create_ci_structure(ca_dir / ci_name, ci_name)
            
            self.stats['cas'] += 1
        
        self.stats['segments'] += 1

    def create_ampel_structure(self, ampel_path, num, code, desc, trl, status, programs, 
                              score, class_, drivers, retrofit, cert, infra):
        """Create AMPEL structure with green potential"""
        ampel_dir = self.create_dir(ampel_path)
        
        # AMPEL documentation with UTCS header and green assessment
        header = self.get_utcs_header("AMPEL", f"AMPEL-{num}-{code}")
        emoji = self.get_green_emoji(score)
        
        content = header + f"""# AMPEL-{num}-{code}: {desc}

## Status & Sustainability
- **Status**: {status} | **TRL**: {trl}
- **Green Potential**: {emoji} {class_} (Score: {score}/100)
- **Active Programs**: {programs}

## Green Technology Integration
### Key Drivers
{chr(10).join([f"- {driver}" for driver in drivers])}

### Integration Assessment
- **Retrofit Feasibility**: {retrofit}
- **Certification Risk**: {cert}
- **Infrastructure Impact**: {infra}

## Technology Roadmap
- Near-term: {"SAF, efficiency improvements" if score >= 60 else "Limited options"}
- Mid-term: {"Hybrid-electric, advanced materials" if score >= 70 else "Incremental improvements"}
- Long-term: {"Full electric/hydrogen" if score >= 75 else "Niche applications"}

## Segments
15 AMEDEO-PELLICCIA technical segments
"""
        
        self.create_file(ampel_dir / "README.md", content)
        
        self.create_yaml(ampel_dir / "ampel-config.yaml", {
            "ampel_id": f"AMPEL-{num}-{code}",
            "description": desc,
            "trl": trl,
            "status": status,
            "active_programs": programs.split(", "),
            "green_potential": {
                "score": score,
                "class": class_,
                "emoji": emoji,
                "drivers": drivers,
                "retrofit_feasibility": retrofit,
                "certification_risk": cert,
                "infrastructure_impact": infra
            },
            "segments": [f"{s[0]}-{s[1]}" for s in self.segments[:self.max_segments]]
        })
        
        # Create limited segments
        for seg_code, seg_name in self.segments[:min(self.max_segments, self.SEGMENT_LIMIT)]:
            segment_dir = f"{seg_code}-{seg_name}"
            self.create_segment_structure(ampel_dir / segment_dir, seg_code, seg_name)
        
        self.stats['ampels'] += 1

    def create_complete_framework(self):
        """Generate complete framework with green potential focus"""
        print("\n" + "="*80)
        print("OPTIM-as-DT: AMEDEO-PELLICCIA Framework V5.0")
        print("Active Programs with Green Potential Assessment")
        print("35 AMPELs | Sustainability Scoring | O/P/T/I/M Structure")
        print("="*80 + "\n")
        
        # Root structure
        print("Creating root structure...")
        for dir_name in [".github", "00-FRAMEWORK", "config", "docs", "scripts", "tests"]:
            self.create_dir(self.base_path / dir_name)
        
        # Create green potential assessment
        print("Creating green potential assessment...")
        self.create_file(self.base_path / "docs" / "GREEN-POTENTIAL-ASSESSMENT.md", 
                        self.create_green_potential_document())
        
        # O-ORGANIZATIONAL Layer
        print("\n[O] Creating ORGANIZATIONAL layer...")
        org_path = self.create_dir(self.base_path / "O-ORGANIZATIONAL")
        for component in ["governance", "sustainability-strategy", "green-metrics", "esg-reporting"]:
            self.create_dir(org_path / component)
        
        # P-PROCEDURAL Layer
        print("[P] Creating PROCEDURAL layer...")
        proc_path = self.create_dir(self.base_path / "P-PROCEDURAL")
        for component in ["green-certification", "sustainability-procedures", "carbon-tracking"]:
            comp_path = self.create_dir(proc_path / component)
        
        # T-TECHNICAL Layer
        print("[T] Creating TECHNICAL layer...")
        tech_base = self.create_dir(self.base_path / "T-TECHNICAL")
        tech_path = self.create_dir(tech_base / "AMEDEO-PELLICCIA")
        
        for domain in ["AIR"]:  # Focus on AIR for green technologies
            print(f"\n  Creating {domain} domain with green focus...")
            domain_path = self.create_dir(tech_path / domain)
            
            # Create AMPELs sorted by green potential
            sorted_ampels = sorted(self.active_ampels_green, key=lambda x: x[6], reverse=True)
            
            print("  Generating 35 AMPELs sorted by green potential...")
            for idx, ampel in enumerate(sorted_ampels[:10], 1):  # Limit to top 10 for demo
                num, code, desc, trl, status, programs, score, class_, drivers, retrofit, cert, infra = ampel
                ampel_name = f"AMPEL-{num}-{code}"
                emoji = self.get_green_emoji(score)
                print(f"    [{idx}/10] {ampel_name} {emoji} (Score: {score})...")
                self.create_ampel_structure(domain_path / ampel_name, 
                                           num, code, desc, trl, status, programs,
                                           score, class_, drivers, retrofit, cert, infra)
            
            # Create Green Technology Registry
            registry_path = self.create_dir(domain_path / "GREEN-REGISTRY")
            
            # YAML registry
            self.create_yaml(registry_path / "green-ampels.yaml", {
                "total_ampels": 35,
                "high_potential": sum(1 for a in self.active_ampels_green if a[6] >= 75),
                "medium_potential": sum(1 for a in self.active_ampels_green if 60 <= a[6] < 75),
                "low_potential": sum(1 for a in self.active_ampels_green if a[6] < 60),
                "ampels": [
                    {
                        "id": f"AMPEL-{a[0]}-{a[1]}",
                        "name": a[2],
                        "trl": a[3],
                        "status": a[4],
                        "programs": a[5],
                        "green_potential": {
                            "score": a[6],
                            "class": a[7],
                            "drivers": a[8],
                            "retrofit_feasibility": a[9],
                            "certification_risk": a[10],
                            "infrastructure_impact": a[11]
                        }
                    } for a in sorted_ampels
                ]
            })
            
            # JSON registry for web apps
            self.create_json(registry_path / "green-ampels.json", {
                "generated": self.timestamp,
                "total": 35,
                "categories": {
                    "high": [{"id": f"AMPEL-{a[0]}-{a[1]}", "score": a[6]} 
                            for a in sorted_ampels if a[6] >= 75],
                    "medium": [{"id": f"AMPEL-{a[0]}-{a[1]}", "score": a[6]} 
                              for a in sorted_ampels if 60 <= a[6] < 75],
                    "low": [{"id": f"AMPEL-{a[0]}-{a[1]}", "score": a[6]} 
                           for a in sorted_ampels if a[6] < 60]
                }
            })
        
        # I-INTELLIGENT Layer
        print("\n[I] Creating INTELLIGENT layer...")
        intel_path = self.create_dir(self.base_path / "I-INTELLIGENT")
        for component in ["green-optimization", "emissions-prediction", "route-efficiency"]:
            comp_path = self.create_dir(intel_path / component)
            self.create_dir(comp_path / "models")
            self.create_dir(comp_path / "algorithms")
        
        # M-MACHINE Layer
        print("[M] Creating MACHINE layer...")
        machine_path = self.create_dir(self.base_path / "M-MACHINE")
        for component in ["emissions-twin", "fuel-optimization", "lifecycle-simulation"]:
            comp_path = self.create_dir(machine_path / component)
            self.create_dir(comp_path / "simulation")
            self.create_dir(comp_path / "monitoring")
        
        # Create main README with green focus
        header = self.get_utcs_header("Framework", "MAIN")
        self.create_file(self.base_path / "README.md", header + f"""# OPTIM-as-DT: Green Aviation Framework V5.0

## Sustainable Aviation Digital Twin Platform

### Framework Focus
- ✅ Active programs with green potential assessment
- ♻️ Sustainability scoring and roadmap
- 🎯 Technology integration pathways
- 📊 Data-driven decarbonization

### Green Potential Distribution
- ♻️ **High Potential** (≥75): {sum(1 for a in self.active_ampels_green if a[6] >= 75)} AMPELs
- ♻︎ **Medium Potential** (60-74): {sum(1 for a in self.active_ampels_green if 60 <= a[6] < 75)} AMPELs
- ◻︎ **Lower Potential** (<60): {sum(1 for a in self.active_ampels_green if a[6] < 60)} AMPELs

### Top Green Technologies
1. **Distributed Propulsion** - Score: 88
2. **Blended Wing Body** - Score: 85
3. **Truss-Braced Wing** - Score: 82
4. **Hydrogen Tube Wing** - Score: 80
5. **Electric STOL** - Score: 77

### Framework Statistics
- Active AMPELs: 35
- Total Segments: {self.stats['segments']:,}
- Configuration Items: {self.stats['cis']:,}
- Files Generated: {self.stats['files']:,}

### O/P/T/I/M Structure
- **O** - Organizational: Sustainability governance
- **P** - Procedural: Green certification processes
- **T** - Technical: AMEDEO-PELLICCIA with green scoring
- **I** - Intelligent: Emissions optimization AI
- **M** - Machine: Carbon footprint digital twin

### Decarbonization Roadmap
#### 2025-2027: Foundation
- SAF deployment at scale
- Retrofit programs for existing fleets
- Electric trainer certification

#### 2027-2030: Transition
- Hybrid-electric regional aircraft
- Urban air mobility deployment
- Advanced aerodynamic configurations

#### 2030-2035: Transformation
- Hydrogen-powered commercial aviation
- Fully electric short-haul
- Autonomous green operations

Generated: {self.timestamp}
Version: 5.0 - Green Potential Focus
""")
        
        # Print summary
        print("\n" + "="*80)
        print("✅ GREEN FRAMEWORK GENERATION COMPLETE!")
        print("="*80)
        print(f"""
Green Potential Summary:
  ♻️ High Potential: {sum(1 for a in self.active_ampels_green if a[6] >= 75)} AMPELs
  ♻︎ Medium Potential: {sum(1 for a in self.active_ampels_green if 60 <= a[6] < 75)} AMPELs
  ◻︎ Lower Potential: {sum(1 for a in self.active_ampels_green if a[6] < 60)} AMPELs
  
Framework Statistics:
  - AMPELs created: {self.stats['ampels']}
  - Segments: {self.stats['segments']:,}
  - Files: {self.stats['files']:,}
  - Directories: {self.stats['directories']:,}
  
Mode: {'DRY RUN' if self.dry else 'FULL GENERATION'}
""")
        print("="*80 + "\n")

def main():
    """Execute with CLI arguments"""
    parser = argparse.ArgumentParser(description="OPTIM-as-DT Green Framework Generator")
    parser.add_argument("--base", default="OPTIM-GREEN", help="Base path for generation")
    parser.add_argument("--domains", nargs="+", default=["AIR"], help="Domains to generate")
    parser.add_argument("--max-segments", type=int, default=5, help="Max segments per AMPEL")
    parser.add_argument("--cas-per-segment", type=int, default=2, help="CAs per segment")
    parser.add_argument("--cis-per-ca", type=int, default=2, help="CIs per CA")
    parser.add_argument("--dry", action="store_true", help="Dry run without creating files")
    parser.add_argument("--top-n", type=int, default=10, help="Generate only top N green AMPELs")
    
    args = parser.parse_args()
    
    generator = OPTIMGreenFramework(
        base_path=args.base,
        max_segments=args.max_segments,
        cas_per_segment=args.cas_per_segment,
        cis_per_ca=args.cis_per_ca,
        dry=args.dry
    )
    
    generator.domains = args.domains
    generator.create_complete_framework()

if __name__ == "__main__":
    main()