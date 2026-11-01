"""
INTERFACE STUB: Maintained by Team 05 (AI & Inspection).
Provided here so Team 02 can test backend core and scoring independently.
"""
from typing import Optional, List
from backend.models.score import CVModelResult

async def run_cv_analysis(image_urls: List[str]) -> Optional[CVModelResult]:
    return CVModelResult(
        predicted_class="clean",
        confidence=0.92,
        structural_score=90.0,
        defects_detected=[],
        defect_coverage_ratio=0.0,
        is_blurry=False
    )
