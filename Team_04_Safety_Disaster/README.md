# NIVAS — Team 04: Safety & Disaster Intelligence

This package contains the NCRB crime statistics, Delhi Police district boundary ray-casting, and the 8-layer national disaster hazard evaluation system.

## Responsibilities
- NCRB 2022 crime statistics & IPC rate resolution (`services/crime_data.py`).
- Delhi Police district boundary point-in-polygon ray-casting (15 districts).
- Nearest police station distance calculation and emergency infrastructure mapping.
- India-wide safety overview dataset and service.
- 8 national disaster hazard layers (`services/disaster.py`):
  1. BIS Seismic Hazard Zones (Zone II to V)
  2. CWC Major Flood Basins
  3. NDMA Coastal Cyclone Hazard Zones
  4. GSI Landslide Susceptibility Zones
  5. IMD Extreme Heatwave Exposure Days
  6. CGWB Groundwater Drought & Water Stress
  7. Yamuna River Floodplain Buffers
  8. Delhi Waterlogging Hotspots
- Multi-locality disaster hazard comparison endpoint.
- Complete test suite with 32 verified tests.

## Quick Start
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/
uvicorn main:app --reload --port 8000
```
