import os
import sys
import types
from typing import Optional
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
if 'backend' not in sys.modules:
    backend_pkg = types.ModuleType('backend')
    backend_pkg.__path__ = [current_dir]
    backend_pkg.__file__ = os.path.join(current_dir, '__init__.py')
    sys.modules['backend'] = backend_pkg

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from backend.api.disaster import router as disaster_router
from backend.services.crime_data import get_locality_safety_data, get_national_safety_overview

app = FastAPI(title='NIVAS Safety & Disaster Intelligence API')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(disaster_router)

@app.get('/api/livability/safety-data')
async def safety_data_endpoint(latitude: float = Query(...), longitude: float = Query(...), address: Optional[str] = Query(None), radius: int = Query(1200)):
    return await get_locality_safety_data(latitude=latitude, longitude=longitude, address=address, radius=radius)

@app.get('/api/livability/national-safety-overview')
async def national_safety_endpoint():
    return get_national_safety_overview()

@app.get('/health')
async def health():
    return {'status': 'ok', 'service': 'NIVAS Safety & Disaster Microservice'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
