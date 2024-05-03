from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base


# SQLAlchemy model for the User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the User
    username = Column(String, unique=True, index=True)  # Unique username
    password = Column(String)  # Hashed password


# SQLAlchemy model for the Task table
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the Task
    title = Column(String, index=True)  # Title of the Task
    description = Column(Text, nullable=True)  # Optional description
    is_completed = Column(Boolean, default=False)  # Task status
    created_at = Column(DateTime, server_default=func.now())  # Timestamp for Task creation
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Reference to User
