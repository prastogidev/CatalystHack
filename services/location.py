"""
INTERFACE STUB: Maintained by Team 03 (Location Intelligence).
Provided here so Team 02 can test backend core and scoring independently.
"""
from typing import Optional
from backend.models.score import LocationResult, InfrastructureSummary

async def fetch_location(address: str, radius_meters: int = 1200) -> Optional[LocationResult]:
    return LocationResult(
        locality=address,
        latitude=28.5921,
        longitude=77.0460,
        risk_score=75.0,
        infrastructure=InfrastructureSummary(hospitals_count=3, schools_count=4, railway_stations_count=2, major_roads_count=8)
    )
