"""
INTERFACE STUB: Maintained by Team 03 (Location Intelligence).
Provided here so Team 02 can test backend core and scoring independently.
"""
from typing import Optional
from backend.models.score import AQIResult

async def fetch_aqi(latitude: float, longitude: float) -> Optional[AQIResult]:
    return AQIResult(
        aqi_value=85.0,
        category="Moderate",
        station_name="Dwarka Sector 8 Station",
        source="WAQI / AQICN",
        environmental_score=75.0,
        fetch_status="active"
    )
