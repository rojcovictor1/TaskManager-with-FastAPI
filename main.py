from fastapi import FastAPI
from app.api.endpoints import users  # Import the router with authentication endpoints
from app.api.endpoints import tasks  # Import the router with tasks endpoints

app = FastAPI()

# Register the authentication router with a prefix
app.include_router(users.router, prefix="/auth")
app.include_router(tasks.router)
