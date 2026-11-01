# Team 02 — Module Scope & Modification Boundaries

## Allowed Modifications
- `services/scoring.py`
- `services/decision.py`
- `services/price.py`
- `services/report.py`
- `services/compare.py`
- `api/score.py`
- `models/score.py`
- `data/cached_demo_data/**`
- `tests/test_price_valuation.py`, `test_decision_layer.py`, `test_report_wording.py`, `test_compare_audit.py`

## Notice on External Domain Services
- `services/location.py`, `services/aqi.py`, `services/cv_model.py`, and `services/thermal.py` are interface stubs provided so that your score evaluation endpoints run independently. Their real implementations are managed by Teams 03 and 05. Do not alter their public signatures.
