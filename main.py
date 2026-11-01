import os
import sys
import types
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
if 'backend' not in sys.modules:
    backend_pkg = types.ModuleType('backend')
    backend_pkg.__path__ = [current_dir]
    backend_pkg.__file__ = os.path.join(current_dir, '__init__.py')
    sys.modules['backend'] = backend_pkg

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.score import router as score_router

app = FastAPI(title='NIVAS Backend Core & Property Scoring API')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(score_router)

@app.get('/health')
async def health():
    return {'status': 'ok', 'service': 'NIVAS Backend Core API'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
