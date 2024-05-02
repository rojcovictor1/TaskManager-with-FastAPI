from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str  # Username for the user
    password: str  # User's password


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True  # This allows Pydantic to work with ORM objects
