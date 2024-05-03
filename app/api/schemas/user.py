from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str  # Username for the user
    password: str  # User's password
    email: EmailStr  # Optional, but useful for additional communication


class UserResponse(BaseModel):
    id: int
    username: str

    # Use 'from_attributes' instead of 'orm_mode' in Pydantic V2 and above
    class Config:
        from_attributes = True  # This allows Pydantic to work with ORM objects


class UserLogin(BaseModel):
    username: str
    password: str
