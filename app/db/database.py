import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")  # Get the database URL from .env

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare the base class for models
Base = declarative_base()