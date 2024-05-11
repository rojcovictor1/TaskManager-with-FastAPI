from fastapi import FastAPI
from fastapi import WebSocket

from app.api.endpoints import tasks  # Import the router with tasks endpoints
from app.api.endpoints import users  # Import the router with authentication endpoints
from app.core.websocket import websocket_endpoint  # Import WebSocket handling and broadcasting

app = FastAPI()

# Register the routers with respective prefixes
app.include_router(users.router, prefix="/auth")
app.include_router(tasks.router)


@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    """WebSocket route that handles WebSocket connections."""
    await websocket_endpoint(websocket)
