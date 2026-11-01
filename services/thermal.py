"""
INTERFACE STUB: Maintained by Team 05 (AI & Inspection).
Provided here so Team 02 can test backend core and scoring independently.
"""
from typing import Optional, List
from backend.models.score import ThermalModuleResult

async def run_thermal_analysis(thermal_data: Optional[List[List[float]]] = None) -> Optional[ThermalModuleResult]:
    return ThermalModuleResult(
        mean_temp=26.4,
        min_temp=24.0,
        max_temp=28.5,
        thermal_anomaly_delta=2.5,
        anomalies_detected_count=0,
        insulation_score=90.0,
        sensor_status="Connected (MLX90640)"
    )
