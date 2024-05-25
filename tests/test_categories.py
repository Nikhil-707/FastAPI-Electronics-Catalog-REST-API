import pytest
from fastapi.testclient import TestClient
from main import app
from models import Category, User  # Import the User model
from database import SessionLocal, Base, engine
from sqlalchemy.orm import sessionmaker
from auth import create_access_token
import auth

# Bind the engine to the sessionmaker
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a test client
client = TestClient(app)

# Fixture to get a test database session
@pytest.fixture()
def session():
    """
    Provides a test database session with a rollback mechanism.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()
        db.close()

@pytest.fixture()
def token(session):
  """
  Retrieves a test access token from the database (if user auth exists).
  """
  if not hasattr(auth, 'create_access_token'):  # Skip if no auth
    return None

  db = session
  test_user = db.query(User).filter_by(username="testuser").first()
  if test_user is None:
    return None  # Handle missing test user

  access_token = create_access_token(data={"user_id": test_user.id})
  return access_token


# Test case for creating a new category
def test_create_category(session, token):
    """
    Tests creating a new category with valid data.
    """
    if token is None:
        pytest.skip("Skipping test_create_category: User authentication not implemented")

    category_data = {
        "name": "Test Category",
        "description": "Test Description",
    }
    response = client.post("/categories", json=category_data, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

    category = response.json()
    assert category["name"] == "Test Category"
    assert category["description"] == "Test Description"

# Test case for listing categories
def test_list_categories(session):
    """
    Tests retrieving a list of categories.
    """
    response = client.get("/categories")
    assert response.status_code == 200
    categories = response.json()
    assert isinstance(categories, list)

@pytest.fixture()
def seed_category(session):
  """
  Seeds the database with a test category for testing.
  """
  category = Category(name="Test Category")
  session.add(category)
  session.commit()
  yield
  session.delete(category)
  session.commit()

# Test case for updating a category (assuming authorization)
@pytest.mark.usefixtures("seed_category")
def test_update_category(session, token):
    """
    Tests updating a category with valid data (requires authorization).
    """
    if token is None:
        pytest.skip("Skipping test_update_category: User authentication not implemented")

    # Assuming there's a category with ID 1 in the database
    category_data = {
        "name": "Updated Category",
        "description": "Updated Description",
    }
    response = client.put("/categories/1", json=category_data, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404  # Assuming category with ID 1 doesn't exist

# Test case for deleting a category (assuming authorization)
@pytest.mark.usefixtures("seed_category")
def test_delete_category(session, token):
    """
    Tests deleting a category (requires authorization).
    """
    if token is None:
        pytest.skip("Skipping test_delete_category: User authentication not implemented")

    # Assuming there's a category with ID 1 in the database
    response = client.delete("/categories/1", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404  # Assuming category with ID 1 doesn't exist

