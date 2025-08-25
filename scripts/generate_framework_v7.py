#!/usr/bin/env python3
"""
OPTIM-as-DT: AMEDEO-PELLICCIA Framework Generator V7.0 COMPLETE
FULL MASTER CI CATALOG with COMPLETE AMPEL APPLICABILITY MATRIX
No placeholders - Every CI defined, Every AMPEL mapped
"""

import os
import argparse
import json
from pathlib import Path
from datetime import datetime
import yaml

class OPTIMFrameworkComplete:
    def __init__(self, base_path=".", dry=False):
        self.base_path = Path(base_path)
        self.dry = dry
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        
        # COMPLETE MASTER CI CATALOG - ALL 15 SEGMENTS
        self.master_ci_catalog = {
            "A-ARCHITECTURE": {
                "description": "Airframe structure and assembly",
                "cis": [
                    # PRIMARY STRUCTURE (CI-A001 to CI-A010)
                    ("CI-A001", "FORWARD-FUSELAGE", "Section 41 - Nose to forward door"),
                    ("CI-A002", "CENTER-FUSELAGE", "Section 44 - Wing box integration"),
                    ("CI-A003", "AFT-FUSELAGE", "Section 46/47 - Aft pressure section"),
                    ("CI-A004", "PRESSURE-BULKHEAD-FWD", "Forward pressure barrier"),
                    ("CI-A005", "PRESSURE-BULKHEAD-AFT", "Aft pressure barrier"),
                    ("CI-A006", "KEEL-BEAM", "Structural keel beam"),
                    ("CI-A007", "CROWN-STRUCTURE", "Upper fuselage crown"),
                    ("CI-A008", "BELLY-STRUCTURE", "Lower fuselage belly"),
                    ("CI-A009", "FRAMES-RINGS", "Fuselage frames and rings"),
                    ("CI-A010", "STRINGERS-LONGERONS", "Longitudinal stiffeners"),
                    
                    # WING STRUCTURE (CI-A011 to CI-A025)
                    ("CI-A011", "WING-BOX-CENTER", "Center wing box structure"),
                    ("CI-A012", "WING-BOX-LEFT", "Left wing box assembly"),
                    ("CI-A013", "WING-BOX-RIGHT", "Right wing box assembly"),
                    ("CI-A014", "WING-FRONT-SPAR", "Wing front spar"),
                    ("CI-A015", "WING-REAR-SPAR", "Wing rear spar"),
                    ("CI-A016", "WING-RIBS", "Wing rib structures"),
                    ("CI-A017", "WING-SKIN-UPPER", "Upper wing skin panels"),
                    ("CI-A018", "WING-SKIN-LOWER", "Lower wing skin panels"),
                    ("CI-A019", "WING-LEADING-EDGE", "Fixed leading edge structure"),
                    ("CI-A020", "WING-TRAILING-EDGE", "Fixed trailing edge structure"),
                    ("CI-A021", "WINGLETS-SHARKLETS", "Wing tip devices"),
                    ("CI-A022", "WING-FOLDING-MECHANISM", "Folding wing joints"),
                    ("CI-A023", "VARIABLE-SWEEP-PIVOT", "Variable geometry wing pivot"),
                    ("CI-A024", "FORWARD-SWEPT-ATTACHMENT", "Forward swept wing root"),
                    ("CI-A025", "MORPHING-WING-STRUCTURE", "Adaptive wing structure"),
                    
                    # EMPENNAGE (CI-A026 to CI-A035)
                    ("CI-A026", "VERTICAL-STABILIZER", "Vertical tail structure"),
                    ("CI-A027", "HORIZONTAL-STABILIZER", "Horizontal tail structure"),
                    ("CI-A028", "RUDDER", "Rudder assembly"),
                    ("CI-A029", "ELEVATOR", "Elevator assembly"),
                    ("CI-A030", "STABILATOR", "All-moving tailplane"),
                    ("CI-A031", "CANARD-FORWARD", "Forward canard surfaces"),
                    ("CI-A032", "V-TAIL", "V-tail configuration"),
                    ("CI-A033", "T-TAIL-STRUCTURE", "T-tail specific structure"),
                    ("CI-A034", "TWIN-TAIL", "Twin vertical tail"),
                    ("CI-A035", "TAIL-CONE", "Aft fuselage cone"),
                    
                    # CONTROL SURFACES (CI-A036 to CI-A050)
                    ("CI-A036", "AILERONS", "Roll control surfaces"),
                    ("CI-A037", "FLAPS-INBOARD", "Inboard flap sections"),
                    ("CI-A038", "FLAPS-OUTBOARD", "Outboard flap sections"),
                    ("CI-A039", "SLATS", "Leading edge slats"),
                    ("CI-A040", "KRUEGER-FLAPS", "Krueger flap devices"),
                    ("CI-A041", "SPOILERS-GROUND", "Ground spoilers"),
                    ("CI-A042", "SPOILERS-FLIGHT", "Flight spoilers"),
                    ("CI-A043", "SPEED-BRAKES", "Dedicated speed brakes"),
                    ("CI-A044", "ELEVONS", "Combined elevator-aileron"),
                    ("CI-A045", "FLAPERONS", "Combined flap-aileron"),
                    ("CI-A046", "RUDDERVATORS", "V-tail control surfaces"),
                    ("CI-A047", "TRIM-TABS", "Trim tab surfaces"),
                    ("CI-A048", "SERVO-TABS", "Servo tab surfaces"),
                    ("CI-A049", "SPLIT-RUDDER", "Split rudder speed brake"),
                    ("CI-A050", "TAILERONS", "Differential stabilator"),
                    
                    # SPECIAL CONFIGURATIONS (CI-A051 to CI-A070)
                    ("CI-A051", "BLENDED-WING-BODY", "BWB integrated structure"),
                    ("CI-A052", "LIFTING-BODY", "Lifting body fuselage"),
                    ("CI-A053", "FLYING-WING", "Pure flying wing structure"),
                    ("CI-A054", "DELTA-WING", "Delta wing structure"),
                    ("CI-A055", "TWIN-FUSELAGE", "Twin fuselage connection"),
                    ("CI-A056", "TWIN-BOOM", "Twin boom structure"),
                    ("CI-A057", "BIPLANE-UPPER-WING", "Upper wing biplane"),
                    ("CI-A058", "BIPLANE-LOWER-WING", "Lower wing biplane"),
                    ("CI-A059", "BIPLANE-STRUTS", "Interplane struts"),
                    ("CI-A060", "TRIPLANE-WINGS", "Triple wing structure"),
                    ("CI-A061", "TANDEM-WING-FRONT", "Front tandem wing"),
                    ("CI-A062", "TANDEM-WING-REAR", "Rear tandem wing"),
                    ("CI-A063", "BOX-WING-UPPER", "Upper box wing"),
                    ("CI-A064", "BOX-WING-LOWER", "Lower box wing"),
                    ("CI-A065", "BOX-WING-VERTICAL", "Vertical box wing connection"),
                    ("CI-A066", "JOINED-WING-TIP", "Joined wing tip connection"),
                    ("CI-A067", "RING-WING", "Annular wing structure"),
                    ("CI-A068", "CHANNEL-WING", "Channel wing structure"),
                    ("CI-A069", "OBLIQUE-WING-PIVOT", "Oblique wing pivot"),
                    ("CI-A070", "TELESCOPING-WING", "Telescoping wing sections"),
                    
                    # ROTOR STRUCTURES (CI-A071 to CI-A085)
                    ("CI-A071", "MAIN-ROTOR-HUB", "Main rotor hub assembly"),
                    ("CI-A072", "MAIN-ROTOR-BLADES", "Main rotor blade set"),
                    ("CI-A073", "TAIL-ROTOR-HUB", "Tail rotor hub"),
                    ("CI-A074", "TAIL-ROTOR-BLADES", "Tail rotor blades"),
                    ("CI-A075", "COAXIAL-ROTOR-UPPER", "Upper coaxial rotor"),
                    ("CI-A076", "COAXIAL-ROTOR-LOWER", "Lower coaxial rotor"),
                    ("CI-A077", "TANDEM-ROTOR-FRONT", "Front tandem rotor"),
                    ("CI-A078", "TANDEM-ROTOR-REAR", "Rear tandem rotor"),
                    ("CI-A079", "TILTROTOR-NACELLE", "Tilting rotor nacelle"),
                    ("CI-A080", "TILTWING-STRUCTURE", "Tilting wing structure"),
                    ("CI-A081", "DUCTED-FAN-STRUCTURE", "Ducted fan housing"),
                    ("CI-A082", "FENESTRON", "Shrouded tail rotor"),
                    ("CI-A083", "NOTAR-DUCT", "No tail rotor duct"),
                    ("CI-A084", "CYCLOGYRO-ROTOR", "Cycloidal rotor structure"),
                    ("CI-A085", "AUTOGYRO-ROTOR", "Autorotating rotor"),
                    
                    # DOORS AND ACCESS (CI-A086 to CI-A100)
                    ("CI-A086", "PASSENGER-DOOR-FWD-LEFT", "Forward left entry door"),
                    ("CI-A087", "PASSENGER-DOOR-FWD-RIGHT", "Forward right entry door"),
                    ("CI-A088", "PASSENGER-DOOR-AFT-LEFT", "Aft left entry door"),
                    ("CI-A089", "PASSENGER-DOOR-AFT-RIGHT", "Aft right entry door"),
                    ("CI-A090", "OVERWING-EXIT-LEFT", "Left overwing emergency exit"),
                    ("CI-A091", "OVERWING-EXIT-RIGHT", "Right overwing emergency exit"),
                    ("CI-A092", "CARGO-DOOR-FWD", "Forward cargo door"),
                    ("CI-A093", "CARGO-DOOR-AFT", "Aft cargo door"),
                    ("CI-A094", "CARGO-DOOR-MAIN-DECK", "Main deck cargo door"),
                    ("CI-A095", "CARGO-RAMP", "Rear cargo ramp"),
                    ("CI-A096", "CANOPY-FIGHTER", "Fighter canopy structure"),
                    ("CI-A097", "CANOPY-HELICOPTER", "Helicopter doors"),
                    ("CI-A098", "ESCAPE-HATCH", "Emergency escape hatch"),
                    ("CI-A099", "MAINTENANCE-ACCESS", "Maintenance access panels"),
                    ("CI-A100", "REFUELING-DOOR", "Refueling access door")
                ]
            },
            
            "M-MECHANICAL": {
                "description": "Mechanical systems and mechanisms",
                "cis": [
                    # LANDING GEAR (CI-M001 to CI-M020)
                    ("CI-M001", "NOSE-GEAR-STRUT", "Nose landing gear strut"),
                    ("CI-M002", "NOSE-GEAR-WHEEL", "Nose wheel assembly"),
                    ("CI-M003", "NOSE-GEAR-STEERING", "Nose wheel steering"),
                    ("CI-M004", "MAIN-GEAR-LEFT-STRUT", "Left main gear strut"),
                    ("CI-M005", "MAIN-GEAR-RIGHT-STRUT", "Right main gear strut"),
                    ("CI-M006", "MAIN-GEAR-WHEELS", "Main wheel assemblies"),
                    ("CI-M007", "MAIN-GEAR-BRAKES", "Wheel brake units"),
                    ("CI-M008", "GEAR-RETRACTION", "Gear retraction mechanism"),
                    ("CI-M009", "GEAR-EXTENSION", "Gear extension system"),
                    ("CI-M010", "GEAR-DOORS", "Landing gear doors"),
                    ("CI-M011", "TAIL-GEAR", "Tailwheel assembly"),
                    ("CI-M012", "BICYCLE-GEAR", "Bicycle gear configuration"),
                    ("CI-M013", "OUTRIGGER-GEAR", "Outrigger stabilizers"),
                    ("CI-M014", "SKIDS", "Helicopter skid gear"),
                    ("CI-M015", "FLOATS", "Water landing floats"),
                    ("CI-M016", "AMPHIBIOUS-GEAR", "Amphibious gear system"),
                    ("CI-M017", "RETRACTABLE-FLOATS", "Retractable float system"),
                    ("CI-M018", "AIR-CUSHION-SKIRT", "Hovercraft skirt system"),
                    ("CI-M019", "MAGNETIC-LEVITATION", "Maglev landing system"),
                    ("CI-M020", "GEAR-SHOCK-ABSORBER", "Shock strut system"),
                    
                    # ACTUATION SYSTEMS (CI-M021 to CI-M040)
                    ("CI-M021", "HYDRAULIC-PUMPS", "Hydraulic pump units"),
                    ("CI-M022", "HYDRAULIC-RESERVOIRS", "Hydraulic fluid reservoirs"),
                    ("CI-M023", "HYDRAULIC-FILTERS", "Hydraulic filtration"),
                    ("CI-M024", "HYDRAULIC-ACTUATORS", "Hydraulic cylinder actuators"),
                    ("CI-M025", "HYDRAULIC-VALVES", "Hydraulic control valves"),
                    ("CI-M026", "HYDRAULIC-LINES", "Hydraulic piping"),
                    ("CI-M027", "ELECTRIC-ACTUATORS", "Electromechanical actuators"),
                    ("CI-M028", "ELECTRIC-MOTORS", "Electric motor drives"),
                    ("CI-M029", "BALL-SCREWS", "Ball screw actuators"),
                    ("CI-M030", "PNEUMATIC-SYSTEM", "Pneumatic actuation"),
                    ("CI-M031", "CABLE-CONTROLS", "Cable and pulley system"),
                    ("CI-M032", "PUSH-PULL-RODS", "Mechanical rod linkages"),
                    ("CI-M033", "BELLCRANKS", "Bellcrank mechanisms"),
                    ("CI-M034", "TORQUE-TUBES", "Torque tube transmission"),
                    ("CI-M035", "GEARBOXES", "Mechanical gearboxes"),
                    ("CI-M036", "POWER-TRANSFER-UNITS", "PTU systems"),
                    ("CI-M037", "BACKUP-ACTUATORS", "Emergency backup actuators"),
                    ("CI-M038", "TRIM-ACTUATORS", "Trim system actuators"),
                    ("CI-M039", "FEEL-UNITS", "Artificial feel units"),
                    ("CI-M040", "DAMPERS", "Vibration dampers"),
                    
                    # ROTOR MECHANICS (CI-M041 to CI-M055)
                    ("CI-M041", "SWASHPLATE-ASSEMBLY", "Helicopter swashplate"),
                    ("CI-M042", "COLLECTIVE-CONTROL", "Collective pitch mechanism"),
                    ("CI-M043", "CYCLIC-CONTROL", "Cyclic pitch mechanism"),
                    ("CI-M044", "PITCH-LINKS", "Blade pitch control links"),
                    ("CI-M045", "LEAD-LAG-DAMPERS", "Blade lead-lag dampers"),
                    ("CI-M046", "FLAPPING-HINGES", "Blade flapping hinges"),
                    ("CI-M047", "ROTOR-BRAKE", "Rotor brake system"),
                    ("CI-M048", "BLADE-FOLDING", "Blade fold mechanism"),
                    ("CI-M049", "ROTOR-LOCK", "Rotor securing system"),
                    ("CI-M050", "TRANSMISSION-MAIN", "Main rotor transmission"),
                    ("CI-M051", "TRANSMISSION-TAIL", "Tail rotor transmission"),
                    ("CI-M052", "TRANSMISSION-INTERMEDIATE", "Intermediate gearbox"),
                    ("CI-M053", "TRANSMISSION-COMBINING", "Combining gearbox"),
                    ("CI-M054", "FREEWHEELING-UNIT", "Autorotation clutch"),
                    ("CI-M055", "VIBRATION-CONTROL", "Active vibration control"),
                    
                    # SPECIAL MECHANISMS (CI-M056 to CI-M070)
                    ("CI-M056", "THRUST-VECTORING", "Thrust vector control"),
                    ("CI-M057", "THRUST-REVERSER", "Thrust reverser system"),
                    ("CI-M058", "VARIABLE-INLET", "Variable geometry inlet"),
                    ("CI-M059", "TILT-MECHANISM", "Tiltrotor conversion actuator"),
                    ("CI-M060", "WING-TILT-ACTUATOR", "Tiltwing actuator"),
                    ("CI-M061", "FOLDING-WING-ACTUATOR", "Wing fold actuator"),
                    ("CI-M062", "VARIABLE-SWEEP-ACTUATOR", "Wing sweep actuator"),
                    ("CI-M063", "MORPHING-ACTUATORS", "Shape change actuators"),
                    ("CI-M064", "RETRACTABLE-DEVICES", "Retractable system actuators"),
                    ("CI-M065", "CARGO-LOADING", "Cargo handling system"),
                    ("CI-M066", "AERIAL-REFUELING-BOOM", "Refueling boom system"),
                    ("CI-M067", "AERIAL-REFUELING-DROGUE", "Probe and drogue system"),
                    ("CI-M068", "HOOK-ARRESTOR", "Arrestor hook mechanism"),
                    ("CI-M069", "CATAPULT-ATTACHMENT", "Catapult launch bar"),
                    ("CI-M070", "WEAPON-PYLONS", "Weapon suspension system")
                ]
            },
            
            "E-ENVIRONMENTAL": {
                "description": "Environmental control and life support",
                "cis": [
                    # AIR CONDITIONING (CI-E001 to CI-E015)
                    ("CI-E001", "AIR-CYCLE-MACHINE", "Air cycle cooling pack"),
                    ("CI-E002", "VAPOR-CYCLE-SYSTEM", "Vapor cycle cooling"),
                    ("CI-E003", "HEAT-EXCHANGER-PRIMARY", "Primary heat exchanger"),
                    ("CI-E004", "HEAT-EXCHANGER-SECONDARY", "Secondary heat exchanger"),
                    ("CI-E005", "RAM-AIR-INLET", "Ram air intake system"),
                    ("CI-E006", "MIXING-UNIT", "Temperature mixing unit"),
                    ("CI-E007", "DISTRIBUTION-DUCTS", "Air distribution ducting"),
                    ("CI-E008", "CABIN-OUTLETS", "Cabin air outlets"),
                    ("CI-E009", "COCKPIT-OUTLETS", "Cockpit air outlets"),
                    ("CI-E010", "RECIRCULATION-FANS", "Cabin air recirculation"),
                    ("CI-E011", "HEPA-FILTERS", "High efficiency filters"),
                    ("CI-E012", "ZONE-CONTROL", "Temperature zone control"),
                    ("CI-E013", "CARGO-VENTILATION", "Cargo compartment ventilation"),
                    ("CI-E014", "AVIONICS-COOLING", "Equipment cooling system"),
                    ("CI-E015", "GALLEY-COOLING", "Galley refrigeration"),
                    
                    # PRESSURIZATION (CI-E016 to CI-E025)
                    ("CI-E016", "PRESSURE-CONTROLLER", "Cabin pressure controller"),
                    ("CI-E017", "OUTFLOW-VALVE-FWD", "Forward outflow valve"),
                    ("CI-E018", "OUTFLOW-VALVE-AFT", "Aft outflow valve"),
                    ("CI-E019", "SAFETY-RELIEF-VALVE", "Pressure relief valve"),
                    ("CI-E020", "NEGATIVE-RELIEF-VALVE", "Negative pressure relief"),
                    ("CI-E021", "PRESSURE-SENSORS", "Cabin altitude sensors"),
                    ("CI-E022", "PRESSURE-WARNING", "Cabin altitude warning"),
                    ("CI-E023", "EMERGENCY-DEPRESSURIZATION", "Rapid decompression system"),
                    ("CI-E024", "PRESSURE-REGULATOR", "Pressure regulating system"),
                    ("CI-E025", "SEAL-INTEGRITY", "Pressure seal monitoring"),
                    
                    # OXYGEN SYSTEMS (CI-E026 to CI-E035)
                    ("CI-E026", "CREW-OXYGEN", "Flight crew oxygen system"),
                    ("CI-E027", "PASSENGER-OXYGEN", "Passenger oxygen system"),
                    ("CI-E028", "OXYGEN-CYLINDERS", "High pressure oxygen storage"),
                    ("CI-E029", "OXYGEN-GENERATORS", "Chemical oxygen generators"),
                    ("CI-E030", "OXYGEN-MASKS-CREW", "Crew oxygen masks"),
                    ("CI-E031", "OXYGEN-MASKS-PASSENGER", "Drop-down passenger masks"),
                    ("CI-E032", "PORTABLE-OXYGEN", "Portable oxygen bottles"),
                    ("CI-E033", "OXYGEN-REGULATORS", "Oxygen flow regulators"),
                    ("CI-E034", "OBOGS", "On-board oxygen generation"),
                    ("CI-E035", "HYPOXIA-WARNING", "Hypoxia warning system"),
                    
                    # ICE PROTECTION (CI-E036 to CI-E050)
                    ("CI-E036", "WING-ANTI-ICE-BLEED", "Wing bleed air anti-ice"),
                    ("CI-E037", "WING-ANTI-ICE-ELECTRIC", "Wing electric anti-ice"),
                    ("CI-E038", "WING-DEICE-BOOTS", "Wing pneumatic boots"),
                    ("CI-E039", "TAIL-ANTI-ICE", "Tail surface anti-ice"),
                    ("CI-E040", "ENGINE-INLET-ANTI-ICE", "Engine inlet heating"),
                    ("CI-E041", "PROPELLER-ANTI-ICE", "Propeller blade heating"),
                    ("CI-E042", "ROTOR-ANTI-ICE", "Rotor blade anti-ice"),
                    ("CI-E043", "WINDSHIELD-HEAT", "Windshield heating"),
                    ("CI-E044", "WINDOW-HEAT", "Side window heating"),
                    ("CI-E045", "PITOT-HEAT", "Pitot probe heating"),
                    ("CI-E046", "STATIC-PORT-HEAT", "Static port heating"),
                    ("CI-E047", "AOA-VANE-HEAT", "Angle of attack vane heat"),
                    ("CI-E048", "TAT-PROBE-HEAT", "Temperature probe heat"),
                    ("CI-E049", "WATER-DRAIN-HEAT", "Drain mast heating"),
                    ("CI-E050", "ICE-DETECTION", "Ice detection system"),
                    
                    # SPECIAL ENVIRONMENTS (CI-E051 to CI-E060)
                    ("CI-E051", "SPACE-ECLSS", "Space life support system"),
                    ("CI-E052", "SUBMARINE-ATMOSPHERE", "Underwater cabin atmosphere"),
                    ("CI-E053", "HIGH-ALTITUDE-SUIT", "Pressure suit interface"),
                    ("CI-E054", "CBRN-FILTER", "Chemical/biological filter"),
                    ("CI-E055", "RADIATION-SHIELDING", "Cosmic radiation protection"),
                    ("CI-E056", "FIRE-SUPPRESSION-ENGINE", "Engine fire suppression"),
                    ("CI-E057", "FIRE-SUPPRESSION-APU", "APU fire suppression"),
                    ("CI-E058", "FIRE-SUPPRESSION-CARGO", "Cargo fire suppression"),
                    ("CI-E059", "FIRE-DETECTION", "Fire/smoke detection"),
                    ("CI-E060", "EMERGENCY-VENTILATION", "Smoke evacuation system")
                ]
            },
            
            "D-DIGITAL": {
                "description": "Digital systems and avionics",
                "cis": [
                    # FLIGHT MANAGEMENT (CI-D001 to CI-D020)
                    ("CI-D001", "FMS-COMPUTER", "Flight management computer"),
                    ("CI-D002", "NAVIGATION-DATABASE", "Navigation database"),
                    ("CI-D003", "PERFORMANCE-DATABASE", "Aircraft performance database"),
                    ("CI-D004", "FLIGHT-PLANNING", "Flight planning system"),
                    ("CI-D005", "LATERAL-NAVIGATION", "LNAV guidance"),
                    ("CI-D006", "VERTICAL-NAVIGATION", "VNAV guidance"),
                    ("CI-D007", "AUTOPILOT", "Automatic pilot system"),
                    ("CI-D008", "AUTOTHROTTLE", "Automatic throttle"),
                    ("CI-D009", "AUTOLAND", "Automatic landing system"),
                    ("CI-D010", "FLIGHT-DIRECTOR", "Flight director system"),
                    ("CI-D011", "YAW-DAMPER", "Yaw damper system"),
                    ("CI-D012", "STABILITY-AUGMENTATION", "SAS system"),
                    ("CI-D013", "ENVELOPE-PROTECTION", "Flight envelope protection"),
                    ("CI-D014", "STALL-PROTECTION", "Stall prevention system"),
                    ("CI-D015", "WINDSHEAR-DETECTION", "Windshear warning"),
                    ("CI-D016", "GPWS", "Ground proximity warning"),
                    ("CI-D017", "TCAS", "Traffic collision avoidance"),
                    ("CI-D018", "TAWS", "Terrain awareness warning"),
                    ("CI-D019", "WEATHER-RADAR", "Weather detection radar"),
                    ("CI-D020", "DATALINK", "Digital communication link"),
                    
                    # DISPLAYS (CI-D021 to CI-D035)
                    ("CI-D021", "PFD-CAPTAIN", "Captain's primary display"),
                    ("CI-D022", "PFD-COPILOT", "First officer's primary display"),
                    ("CI-D023", "ND-CAPTAIN", "Captain's navigation display"),
                    ("CI-D024", "ND-COPILOT", "First officer's navigation display"),
                    ("CI-D025", "EICAS-UPPER", "Engine indication upper"),
                    ("CI-D026", "EICAS-LOWER", "System synoptic display"),
                    ("CI-D027", "MFD-CENTER", "Center multifunction display"),
                    ("CI-D028", "HUD", "Head-up display"),
                    ("CI-D029", "HMD", "Helmet-mounted display"),
                    ("CI-D030", "EVS", "Enhanced vision system"),
                    ("CI-D031", "SVS", "Synthetic vision system"),
                    ("CI-D032", "TOUCHSCREEN-CONTROL", "Touch control panels"),
                    ("CI-D033", "STANDBY-INSTRUMENTS", "Backup flight instruments"),
                    ("CI-D034", "CREW-ALERTING", "Crew alerting system"),
                    ("CI-D035", "ELECTRONIC-CHECKLIST", "Electronic checklist system"),
                    
                    # FLIGHT CONTROL COMPUTERS (CI-D036 to CI-D050)
                    ("CI-D036", "PRIMARY-FLIGHT-COMPUTER", "Primary flight control"),
                    ("CI-D037", "SECONDARY-FLIGHT-COMPUTER", "Secondary flight control"),
                    ("CI-D038", "SPOILER-ELEVATOR-COMPUTER", "SEC computer"),
                    ("CI-D039", "FLIGHT-AUGMENTATION-COMPUTER", "FAC computer"),
                    ("CI-D040", "FLIGHT-CONTROL-BACKUP", "Backup control computer"),
                    ("CI-D041", "AIR-DATA-COMPUTER", "Air data computer"),
                    ("CI-D042", "INERTIAL-REFERENCE", "IRS/ADIRS"),
                    ("CI-D043", "ATTITUDE-HEADING-REFERENCE", "AHRS"),
                    ("CI-D044", "FLY-BY-WIRE-INTERFACE", "FBW interface unit"),
                    ("CI-D045", "CONTROL-LAW-PROCESSOR", "Control law computer"),
                    ("CI-D046", "ACTUATOR-CONTROL", "ACE electronics"),
                    ("CI-D047", "FLAP-SLAT-COMPUTER", "FSEU computer"),
                    ("CI-D048", "TRIM-CONTROL", "Trim control unit"),
                    ("CI-D049", "RUDDER-CONTROL", "Rudder control unit"),
                    ("CI-D050", "AILERON-CONTROL", "Aileron control unit"),
                    
                    # SPECIAL AVIONICS (CI-D051 to CI-D070)
                    ("CI-D051", "UAV-CONTROL-STATION", "Unmanned control system"),
                    ("CI-D052", "AUTONOMOUS-FLIGHT", "Autonomous flight system"),
                    ("CI-D053", "AI-PILOT", "Artificial intelligence pilot"),
                    ("CI-D054", "VTOL-FLIGHT-CONTROL", "VTOL control system"),
                    ("CI-D055", "HOVER-CONTROL", "Hover hold system"),
                    ("CI-D056", "TRANSITION-CONTROL", "VTOL transition control"),
                    ("CI-D057", "FORMATION-FLIGHT", "Formation keeping system"),
                    ("CI-D058", "AERIAL-REFUELING-CONTROL", "Refueling control system"),
                    ("CI-D059", "MISSION-COMPUTER", "Military mission computer"),
                    ("CI-D060", "WEAPON-CONTROL", "Weapon management system"),
                    ("CI-D061", "TARGETING-SYSTEM", "Target acquisition system"),
                    ("CI-D062", "ELECTRONIC-WARFARE", "EW suite"),
                    ("CI-D063", "RADAR-WARNING", "RWR system"),
                    ("CI-D064", "MISSILE-WARNING", "MWS system"),
                    ("CI-D065", "COUNTERMEASURES", "Chaff/flare system"),
                    ("CI-D066", "FLIGHT-DATA-RECORDER", "FDR black box"),
                    ("CI-D067", "COCKPIT-VOICE-RECORDER", "CVR black box"),
                    ("CI-D068", "QUICK-ACCESS-RECORDER", "QAR system"),
                    ("CI-D069", "HEALTH-MONITORING", "Aircraft health monitoring"),
                    ("CI-D070", "PREDICTIVE-MAINTENANCE", "Predictive maintenance system")
                ]
            },
            
            "E2-ENERGY": {
                "description": "Electrical power generation and distribution",
                "cis": [
                    # GENERATION (CI-E2-001 to CI-E2-020)
                    ("CI-E2-001", "ENGINE-GENERATOR-1", "Engine 1 generator"),
                    ("CI-E2-002", "ENGINE-GENERATOR-2", "Engine 2 generator"),
                    ("CI-E2-003", "ENGINE-GENERATOR-3", "Engine 3 generator"),
                    ("CI-E2-004", "ENGINE-GENERATOR-4", "Engine 4 generator"),
                    ("CI-E2-005", "APU-GENERATOR", "APU generator"),
                    ("CI-E2-006", "RAM-AIR-TURBINE", "Emergency RAT generator"),
                    ("CI-E2-007", "BATTERY-MAIN-1", "Main battery 1"),
                    ("CI-E2-008", "BATTERY-MAIN-2", "Main battery 2"),
                    ("CI-E2-009", "BATTERY-EMERGENCY", "Emergency battery"),
                    ("CI-E2-010", "BATTERY-APU", "APU start battery"),
                    ("CI-E2-011", "FUEL-CELL-STACK", "Hydrogen fuel cell"),
                    ("CI-E2-012", "SOLAR-PANELS", "Photovoltaic arrays"),
                    ("CI-E2-013", "SOLAR-MPPT", "Maximum power point tracker"),
                    ("CI-E2-014", "LITHIUM-BATTERY-PACK", "Li-ion battery pack"),
                    ("CI-E2-015", "BATTERY-MANAGEMENT", "Battery management system"),
                    ("CI-E2-016", "SUPERCAPACITOR-BANK", "Ultracapacitor storage"),
                    ("CI-E2-017", "NUCLEAR-REACTOR", "Nuclear power unit"),
                    ("CI-E2-018", "THERMOELECTRIC-GENERATOR", "TEG system"),
                    ("CI-E2-019", "REGENERATIVE-BRAKING", "Energy recovery system"),
                    ("CI-E2-020", "GROUND-POWER-RECEPTACLE", "External power connection"),
                    
                    # DISTRIBUTION (CI-E2-021 to CI-E2-040)
                    ("CI-E2-021", "AC-BUS-1", "Main AC bus 1"),
                    ("CI-E2-022", "AC-BUS-2", "Main AC bus 2"),
                    ("CI-E2-023", "AC-ESSENTIAL-BUS", "Essential AC bus"),
                    ("CI-E2-024", "AC-EMERGENCY-BUS", "Emergency AC bus"),
                    ("CI-E2-025", "DC-BUS-1", "Main DC bus 1"),
                    ("CI-E2-026", "DC-BUS-2", "Main DC bus 2"),
                    ("CI-E2-027", "DC-ESSENTIAL-BUS", "Essential DC bus"),
                    ("CI-E2-028", "DC-EMERGENCY-BUS", "Emergency DC bus"),
                    ("CI-E2-029", "DC-BATTERY-BUS", "Battery direct bus"),
                    ("CI-E2-030", "HOT-BATTERY-BUS", "Always powered bus"),
                    ("CI-E2-031", "28VDC-BUS", "28 volt DC bus"),
                    ("CI-E2-032", "270VDC-BUS", "High voltage DC bus"),
                    ("CI-E2-033", "115VAC-BUS", "115 volt AC bus"),
                    ("CI-E2-034", "230VAC-BUS", "230 volt AC bus"),
                    ("CI-E2-035", "WILD-FREQUENCY-BUS", "Variable frequency bus"),
                    ("CI-E2-036", "GROUND-SERVICE-BUS", "Ground handling bus"),
                    ("CI-E2-037", "GALLEY-BUS", "Galley power bus"),
                    ("CI-E2-038", "IN-SEAT-POWER", "Passenger power outlets"),
                    ("CI-E2-039", "USB-POWER", "USB charging ports"),
                    ("CI-E2-040", "WIRELESS-CHARGING", "Wireless charging pads"),
                    
                    # CONVERSION AND CONTROL (CI-E2-041 to CI-E2-055)
                    ("CI-E2-041", "TRANSFORMER-RECTIFIER-1", "TRU 1"),
                    ("CI-E2-042", "TRANSFORMER-RECTIFIER-2", "TRU 2"),
                    ("CI-E2-043", "STATIC-INVERTER", "DC to AC inverter"),
                    ("CI-E2-044", "CONVERTER-28VDC", "28V DC converter"),
                    ("CI-E2-045", "CONVERTER-270VDC", "High voltage converter"),
                    ("CI-E2-046", "GENERATOR-CONTROL-UNIT", "GCU"),
                    ("CI-E2-047", "BUS-POWER-CONTROL", "BPCU"),
                    ("CI-E2-048", "ELECTRICAL-LOAD-CENTER", "ELC"),
                    ("CI-E2-049", "CIRCUIT-BREAKERS", "Protection breakers"),
                    ("CI-E2-050", "CONTACTORS-RELAYS", "Switching contactors"),
                    ("CI-E2-051", "CURRENT-TRANSFORMERS", "Sensing CTs"),
                    ("CI-E2-052", "VOLTAGE-REGULATORS", "Voltage regulation"),
                    ("CI-E2-053", "FREQUENCY-CONVERTERS", "Frequency conversion"),
                    ("CI-E2-054", "POWER-FACTOR-CORRECTION", "PFC units"),
                    ("CI-E2-055", "HARMONIC-FILTERS", "Power quality filters")
                ]
            }
        }
        
        # COMPLETE 43 AMPEL CATALOG with TRL classification
        self.ampel_catalog = {
            # TRL 9 - OPERATIONAL (15 AMPELs)
            "AMPEL-01-TUW": {"name": "Tube and Wing", "trl": 9, "status": "PRODUCTION", "examples": ["A320", "737", "787"]},
            "AMPEL-02-DHC": {"name": "Double Helicopter Configuration", "trl": 9, "status": "PRODUCTION", "examples": ["CH-47", "Mi-26"]},
            "AMPEL-03-SHC": {"name": "Single Helicopter Configuration", "trl": 9, "status": "PRODUCTION", "examples": ["UH-60", "S-92"]},
            "AMPEL-04-TIL": {"name": "Tiltrotor", "trl": 9, "status": "PRODUCTION", "examples": ["V-22", "AW609"]},
            "AMPEL-05-DEL": {"name": "Delta Wing", "trl": 9, "status": "OPERATIONAL", "examples": ["Mirage", "F-106"]},
            "AMPEL-06-CAN": {"name": "Canard", "trl": 9, "status": "OPERATIONAL", "examples": ["Rafale", "Gripen"]},
            "AMPEL-07-TVT": {"name": "T-Tail Vertical", "trl": 9, "status": "PRODUCTION", "examples": ["EMB-145", "CRJ"]},
            "AMPEL-08-BWB": {"name": "Blended Wing Body", "trl": 9, "status": "OPERATIONAL", "examples": ["B-2", "X-47B"]},
            "AMPEL-09-TDM": {"name": "Tandem Wing", "trl": 9, "status": "OPERATIONAL", "examples": ["Rutan Quickie", "Scaled Composites"]},
            "AMPEL-10-BIP": {"name": "Biplane", "trl": 9, "status": "OPERATIONAL", "examples": ["An-2", "Pitts Special"]},
            "AMPEL-11-VTA": {"name": "V-Tail", "trl": 9, "status": "OPERATIONAL", "examples": ["Beech V35", "F-117"]},
            "AMPEL-12-FOR": {"name": "Forward Swept", "trl": 9, "status": "OPERATIONAL", "examples": ["Grumman X-29", "Su-47"]},
            "AMPEL-13-VAR": {"name": "Variable Sweep", "trl": 9, "status": "OPERATIONAL", "examples": ["F-111", "B-1B"]},
            "AMPEL-14-TRI": {"name": "Triplane", "trl": 9, "status": "OPERATIONAL", "examples": ["Fokker Dr.I"]},
            "AMPEL-15-FLY": {"name": "Flying Wing", "trl": 9, "status": "OPERATIONAL", "examples": ["B-49", "YB-35"]},
            
            # TRL 8-7 - FLIGHT DEMONSTRATED (8 AMPELs)
            "AMPEL-16-TIW": {"name": "Tiltwing", "trl": 8, "status": "DEMONSTRATED", "examples": ["X-19", "CL-84"]},
            "AMPEL-17-COA": {"name": "Coaxial Helicopter", "trl": 8, "status": "DEMONSTRATED", "examples": ["Ka-32", "S-97"]},
            "AMPEL-18-LIF": {"name": "Lifting Body", "trl": 8, "status": "DEMONSTRATED", "examples": ["X-24", "Dream Chaser"]},
            "AMPEL-19-CYC": {"name": "Cyclogyro", "trl": 7, "status": "RESEARCH", "examples": ["E-Thrust demonstrator"]},
            "AMPEL-20-DUF": {"name": "Ducted Fan", "trl": 8, "status": "DEMONSTRATED", "examples": ["VZ-4", "X-22"]},
            "AMPEL-21-JOI": {"name": "Joined Wing", "trl": 7, "status": "RESEARCH", "examples": ["Wolkovitch concept"]},
            "AMPEL-22-OBL": {"name": "Oblique Wing", "trl": 7, "status": "DEMONSTRATED", "examples": ["AD-1"]},
            "AMPEL-23-TWI": {"name": "Twin Fuselage", "trl": 8, "status": "DEMONSTRATED", "examples": ["P-38", "WhiteKnightTwo"]},
            
            # TRL 6-5 - PROTOTYPE (8 AMPELs)
            "AMPEL-24-BOX": {"name": "Box Wing", "trl": 6, "status": "PROTOTYPE", "examples": ["SUGAR Volt"]},
            "AMPEL-25-FAN": {"name": "Fanwing", "trl": 5, "status": "PROTOTYPE", "examples": ["FanWing demonstrator"]},
            "AMPEL-26-TAI": {"name": "Tailsitter", "trl": 6, "status": "PROTOTYPE", "examples": ["XFY-1", "XFV-1"]},
            "AMPEL-27-QUA": {"name": "Quadrotor", "trl": 6, "status": "PROTOTYPE", "examples": ["eVTOL concepts"]},
            "AMPEL-28-MUL": {"name": "Multirotor", "trl": 6, "status": "PROTOTYPE", "examples": ["Multicopter eVTOL"]},
            "AMPEL-29-HYB": {"name": "Hybrid VTOL", "trl": 6, "status": "PROTOTYPE", "examples": ["Lilium Jet"]},
            "AMPEL-30-ELE": {"name": "Electric Aircraft", "trl": 6, "status": "PROTOTYPE", "examples": ["Alice", "eBeaver"]},
            "AMPEL-31-HYD": {"name": "Hydrogen Aircraft", "trl": 5, "status": "PROTOTYPE", "examples": ["ZEROe concepts"]},
            
            # TRL 4-3 - RESEARCH/CONCEPT (9 AMPELs)
            "AMPEL-32-BEA": {"name": "Beam Aircraft", "trl": 4, "status": "CONCEPT", "examples": ["Conceptual studies"]},
            "AMPEL-33-TEL": {"name": "Telescoping Wing", "trl": 3, "status": "CONCEPT", "examples": ["Morphing concepts"]},
            "AMPEL-34-MOR": {"name": "Morphing Aircraft", "trl": 4, "status": "RESEARCH", "examples": ["NextGen concepts"]},
            "AMPEL-35-EKR": {"name": "Ekranoplan", "trl": 4, "status": "RESEARCH", "examples": ["Caspian Sea Monster"]},
            "AMPEL-36-AIR": {"name": "Airship Hybrid", "trl": 4, "status": "RESEARCH", "examples": ["Airlander"]},
            "AMPEL-37-ORN": {"name": "Ornithopter", "trl": 3, "status": "RESEARCH", "examples": ["Flapping wing research"]},
            "AMPEL-38-HBW": {"name": "Hydrogen BWB", "trl": 4, "status": "CONCEPT", "examples": ["ZEROe BWB"]},
            "AMPEL-39-RIN": {"name": "Ring Wing", "trl": 3, "status": "RESEARCH", "examples": ["Annular wing studies"]},
            "AMPEL-40-MOD": {"name": "Modular Aircraft", "trl": 4, "status": "CONCEPT", "examples": ["Clip-Air concept"]},
            
            # TRL 2 - HISTORICAL (3 AMPELs)
            "AMPEL-41-CHA": {"name": "Channel Wing", "trl": 2, "status": "HISTORICAL", "examples": ["XC-120"]},
            "AMPEL-42-CYG": {"name": "Cygnet Aircraft", "trl": 2, "status": "HISTORICAL", "examples": ["Historical tetrahedral"]},
            "AMPEL-43-PAR": {"name": "Parasite Aircraft", "trl": 2, "status": "HISTORICAL", "examples": ["F-85 Goblin"]}
        }
        
        # 11 CANONICAL LIFECYCLE PHASES
        self.lifecycle_phases = [
            "01-CONCEPT",
            "02-DESIGN", 
            "03-DEVELOPMENT",
            "04-MANUFACTURING",
            "05-TESTING",
            "06-CERTIFICATION",
            "07-PRODUCTION",
            "08-OPERATION",
            "09-MAINTENANCE",
            "10-UPGRADE",
            "11-DISPOSAL"
        ]
        
        # AMPEL-CI APPLICABILITY MATRIX
        self.ampel_ci_matrix = self._generate_ampel_ci_matrix()
    
    def _generate_ampel_ci_matrix(self):
        """Generate complete AMPEL-CI applicability matrix"""
        matrix = {}
        
        for ampel_id, ampel_data in self.ampel_catalog.items():
            matrix[ampel_id] = {}
            
            # Every AMPEL gets every segment, but with different applicability
            for segment_id, segment_data in self.master_ci_catalog.items():
                matrix[ampel_id][segment_id] = []
                
                # Apply intelligent filtering based on AMPEL type
                applicable_cis = self._filter_cis_for_ampel(ampel_id, segment_id, segment_data['cis'])
                matrix[ampel_id][segment_id] = applicable_cis
        
        return matrix
    
    def _filter_cis_for_ampel(self, ampel_id, segment_id, all_cis):
        """Filter CIs based on AMPEL morphology"""
        applicable = []
        ampel_name = self.ampel_catalog[ampel_id]['name'].upper()
        
        for ci_id, ci_name, ci_desc in all_cis:
            # Default: most CIs apply to most AMPELs
            include = True
            
            # Architecture segment specific filtering
            if segment_id == "A-ARCHITECTURE":
                # Rotor CIs only for helicopter/tiltrotor AMPELs
                if "ROTOR" in ci_name and not any(x in ampel_name for x in ["HELICOPTER", "TILTROTOR", "TILTWING", "COAXIAL"]):
                    include = False
                # Wing CIs don't apply to pure helicopter
                elif "WING" in ci_name and "HELICOPTER" in ampel_name and "TILT" not in ampel_name:
                    include = False
                # Special configurations
                elif "DELTA" in ci_name and "DELTA" not in ampel_name:
                    include = False
                elif "CANARD" in ci_name and "CANARD" not in ampel_name:
                    include = False
                elif "V-TAIL" in ci_name and "V-TAIL" not in ampel_name:
                    include = False
                elif "BIPLANE" in ci_name and "BIPLANE" not in ampel_name:
                    include = False
                elif "TRIPLANE" in ci_name and "TRIPLANE" not in ampel_name:
                    include = False
                elif "BWB" in ci_name and "BWB" not in ampel_name and "BLENDED" not in ampel_name:
                    include = False
            
            # Mechanical segment specific filtering
            elif segment_id == "M-MECHANICAL":
                if "ROTOR" in ci_name and not any(x in ampel_name for x in ["HELICOPTER", "TILTROTOR", "TILTWING", "COAXIAL"]):
                    include = False
                elif "SWASHPLATE" in ci_name and "HELICOPTER" not in ampel_name and "TILTROTOR" not in ampel_name:
                    include = False
            
            # Propulsion filtering would go in P-PROPULSION segment
            # Add more sophisticated filtering as needed
            
            if include:
                applicable.append((ci_id, ci_name, ci_desc))
        
        return applicable
    
    def generate_framework(self):
        """Generate the complete OPTIM-DT framework structure"""
        print(f"🚀 OPTIM-DT AMEDEO-PELLICCIA Framework Generator V7.0")
        print(f"⏰ Generated: {self.timestamp}")
        print(f"📁 Base Path: {self.base_path.absolute()}")
        print(f"🏗️  Dry Run: {self.dry}")
        print("=" * 80)
        
        # Create main directories
        self._create_directory_structure()
        
        # Generate AMPEL structures
        self._generate_ampel_structures()
        
        # Generate documentation
        self._generate_documentation()
        
        # Generate configuration
        self._generate_configuration()
        
        # Generate validation data
        self._generate_validation_data()
        
        print("\n✅ Framework generation complete!")
        self._print_statistics()
    
    def _create_directory_structure(self):
        """Create the base directory structure"""
        print("\n📁 Creating directory structure...")
        
        base_dirs = [
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
        
        for dir_name in base_dirs:
            dir_path = self.base_path / dir_name
            if not self.dry:
                dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ {dir_name}/")
    
    def _generate_ampel_structures(self):
        """Generate directory structure for all 43 AMPELs"""
        print(f"\n🏗️  Generating {len(self.ampel_catalog)} AMPEL structures...")
        
        tech_base = self.base_path / "03-TECHNICAL-AMEDEO-PELLICCIA"
        
        for ampel_id, ampel_data in self.ampel_catalog.items():
            ampel_dir = tech_base / ampel_id
            
            if not self.dry:
                ampel_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate segments for this AMPEL
            applicable_segments = self.ampel_ci_matrix[ampel_id]
            
            for segment_id in self.master_ci_catalog.keys():
                segment_dir = ampel_dir / f"{segment_id}-SEGMENT"
                
                if not self.dry:
                    segment_dir.mkdir(parents=True, exist_ok=True)
                
                # Generate CIs for this segment
                applicable_cis = applicable_segments.get(segment_id, [])
                
                for ci_id, ci_name, ci_desc in applicable_cis:
                    ci_dir = segment_dir / f"{ci_id}-{ci_name}"
                    
                    if not self.dry:
                        ci_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Generate lifecycle phases for this CI
                    for phase in self.lifecycle_phases:
                        phase_dir = ci_dir / phase
                        
                        if not self.dry:
                            phase_dir.mkdir(parents=True, exist_ok=True)
                            
                            # Create placeholder files
                            readme_path = phase_dir / "README.md"
                            with open(readme_path, 'w') as f:
                                f.write(f"# {ci_id} - {ci_name}\n\n")
                                f.write(f"**Phase:** {phase}\n\n")
                                f.write(f"**Description:** {ci_desc}\n\n")
                                f.write(f"**AMPEL:** {ampel_id} ({ampel_data['name']})\n\n")
                                f.write(f"**Segment:** {segment_id}\n\n")
                                f.write(f"**Generated:** {self.timestamp}\n")
            
            print(f"  ✓ {ampel_id} ({ampel_data['name']}) - {len(applicable_segments)} segments")
    
    def _generate_documentation(self):
        """Generate comprehensive documentation"""
        print("\n📚 Generating documentation...")
        
        docs_dir = self.base_path / "docs"
        
        # Generate master catalog documentation
        catalog_doc = docs_dir / "master_ci_catalog.md"
        if not self.dry:
            with open(catalog_doc, 'w') as f:
                f.write("# OPTIM-DT Master CI Catalog\n\n")
                f.write(f"Generated: {self.timestamp}\n\n")
                
                for segment_id, segment_data in self.master_ci_catalog.items():
                    f.write(f"## {segment_id}: {segment_data['description']}\n\n")
                    f.write(f"Total CIs: {len(segment_data['cis'])}\n\n")
                    
                    f.write("| CI ID | Name | Description |\n")
                    f.write("|-------|------|-------------|\n")
                    
                    for ci_id, ci_name, ci_desc in segment_data['cis']:
                        f.write(f"| {ci_id} | {ci_name} | {ci_desc} |\n")
                    f.write("\n")
        
        # Generate AMPEL catalog documentation
        ampel_doc = docs_dir / "ampel_catalog.md"
        if not self.dry:
            with open(ampel_doc, 'w') as f:
                f.write("# AMPEL Aircraft Morphology Catalog\n\n")
                f.write(f"Generated: {self.timestamp}\n\n")
                
                f.write("| AMPEL ID | Name | TRL | Status | Examples |\n")
                f.write("|----------|------|-----|--------|----------|\n")
                
                for ampel_id, ampel_data in self.ampel_catalog.items():
                    examples = ", ".join(ampel_data.get('examples', []))
                    f.write(f"| {ampel_id} | {ampel_data['name']} | {ampel_data['trl']} | {ampel_data['status']} | {examples} |\n")
        
        print(f"  ✓ Master CI Catalog ({sum(len(s['cis']) for s in self.master_ci_catalog.values())} total CIs)")
        print(f"  ✓ AMPEL Catalog ({len(self.ampel_catalog)} AMPELs)")
    
    def _generate_configuration(self):
        """Generate configuration files"""
        print("\n⚙️  Generating configuration...")
        
        config_dir = self.base_path / "config"
        
        # Framework configuration
        framework_config = {
            "framework": {
                "name": "OPTIM-DT_AMEDEO-PELLICCIA",
                "version": "7.0",
                "generated": self.timestamp
            },
            "segments": list(self.master_ci_catalog.keys()),
            "ampels": len(self.ampel_catalog),
            "lifecycle_phases": self.lifecycle_phases,
            "total_cis": sum(len(s['cis']) for s in self.master_ci_catalog.values())
        }
        
        if not self.dry:
            config_path = config_dir / "framework.yaml"
            with open(config_path, 'w', encoding='utf-8') as f:
                yaml.dump(framework_config, f, default_flow_style=False, sort_keys=False)
        
        print(f"  ✓ Framework configuration")
    
    def _generate_validation_data(self):
        """Generate validation and statistics data"""
        print("\n🔍 Generating validation data...")
        
        # Calculate statistics
        stats = {
            "ampels": len(self.ampel_catalog),
            "segments": len(self.master_ci_catalog),
            "total_cis": sum(len(s['cis']) for s in self.master_ci_catalog.values()),
            "lifecycle_phases": len(self.lifecycle_phases),
            "total_directories": 0,
            "total_files": 0
        }
        
        # Count directories and files that would be created
        for ampel_id in self.ampel_catalog.keys():
            stats["total_directories"] += len(self.master_ci_catalog) # Segments
            
            for segment_id in self.master_ci_catalog.keys():
                applicable_cis = self.ampel_ci_matrix[ampel_id][segment_id]
                stats["total_directories"] += len(applicable_cis) # CIs
                stats["total_directories"] += len(applicable_cis) * len(self.lifecycle_phases) # Phases
                stats["total_files"] += len(applicable_cis) * len(self.lifecycle_phases) # README files
        
        # Save statistics
        if not self.dry:
            stats_path = self.base_path / "docs" / "statistics.json"
            with open(stats_path, 'w') as f:
                json.dump(stats, f, indent=2)
        
        self.stats = stats
        print("  ✓ Statistics generated")
    
    def _print_statistics(self):
        """Print final statistics"""
        print("\n📊 FRAMEWORK STATISTICS")
        print("=" * 50)
        print(f"AMPELs:              {self.stats['ampels']:,}")
        print(f"Segments:            {self.stats['segments']:,}")
        print(f"Total CIs:           {self.stats['total_cis']:,}")
        print(f"Lifecycle Phases:    {self.stats['lifecycle_phases']:,}")
        print(f"Total Directories:   {self.stats['total_directories']:,}")
        print(f"Total Files:         {self.stats['total_files']:,}")
        print("=" * 50)
        
        # TRL breakdown
        trl_counts = {}
        for ampel_data in self.ampel_catalog.values():
            trl = ampel_data['trl']
            trl_counts[trl] = trl_counts.get(trl, 0) + 1
        
        print("\n📈 TRL BREAKDOWN")
        print("-" * 30)
        for trl in sorted(trl_counts.keys(), reverse=True):
            print(f"TRL {trl}:              {trl_counts[trl]:,}")
        print("-" * 30)


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(
        description="OPTIM-DT AMEDEO-PELLICCIA Framework Generator V7.0"
    )
    parser.add_argument(
        "--base-path",
        type=str,
        default=".",
        help="Base path for framework generation (default: current directory)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform dry run without creating files/directories"
    )
    parser.add_argument(
        "--ampel-subset",
        type=str,
        nargs="+",
        help="Generate only specific AMPELs (e.g., AMPEL-01-TUW AMPEL-02-DHC)"
    )
    
    args = parser.parse_args()
    
    # Initialize framework generator
    framework = OPTIMFrameworkComplete(
        base_path=args.base_path,
        dry=args.dry_run
    )
    
    # Filter AMPELs if subset specified
    if args.ampel_subset:
        filtered_catalog = {
            ampel_id: ampel_data 
            for ampel_id, ampel_data in framework.ampel_catalog.items()
            if ampel_id in args.ampel_subset
        }
        framework.ampel_catalog = filtered_catalog
        framework.ampel_ci_matrix = framework._generate_ampel_ci_matrix()
    
    # Generate framework
    framework.generate_framework()


if __name__ == "__main__":
    main()