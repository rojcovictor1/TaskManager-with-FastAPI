# db/database.py
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # Get the database URL from .env

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a scoped session for tests
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Declare the base class for models
Base = declarative_base()
