from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.sql import func
from app.db.database import Base


# SQLAlchemy model for the User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Primary key, unique identifier
    username = Column(String, unique=True, index=True)  # User's username, unique and indexed
    password = Column(String)  # User's hashed password


# SQLAlchemy model for the Task table
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)  # Primary key, unique identifier
    title = Column(String, index=True)  # Task title, indexed
    description = Column(Text, nullable=True)  # Task description (optional)
    is_completed = Column(Boolean, default=False)  # Task status (completed or not)
    created_at = Column(DateTime, server_default=func.now())  # Timestamp for task creation
    user_id = Column(Integer, nullable=False)  # Foreign key linking to User
