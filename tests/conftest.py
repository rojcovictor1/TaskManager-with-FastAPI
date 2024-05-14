# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from app.db.database import engine
from app.db.dependencies import get_db
from main import app


@pytest.fixture(scope="function")
def db_session():
    # Create a new database session with a transaction for each test
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db_session):
    # Dependency override for the testing session
    def override_get_db():
        try:
            yield db_session
        finally:
            pass  # normally you might close the session here, but we'll close it in the fixture

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
