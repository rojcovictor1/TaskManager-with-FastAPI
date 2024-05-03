from fastapi import FastAPI
from app.api.endpoints import users  # Import the router with authentication endpoints

app = FastAPI()

# Register the authentication router with a prefix
app.include_router(users.router, prefix="/auth")
