# NIVAS — Team 02: Backend Core & Property Scoring

This package contains the core FastAPI architecture, composite property scoring engine, and valuation intelligence for NIVAS.

## Responsibilities
- FastAPI gateway application (`main.py`) with CORS, timing middleware, and global error handling.
- Composite property scoring algorithm (`scoring.py`): Weighted evaluation across defects, thermal, location, and environment.
- Explainable decision layer (`decision.py`): Risk flags, investment confidence score, and clear recommendation rationale.
- Property valuation service (`price.py`): Propstack API client, circle rate calculation, and cached local benchmarks (Dwarka, Rohini, Lajpat Nagar).
- Comprehensive inspection report generator (`report.py`).
- Symmetric property comparison engine (`compare.py`).
- Core Pydantic schemas (`models/score.py`).

## Quick Start
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/
uvicorn main:app --reload --port 8000
```
