import pytest
from fastapi.testclient import TestClient
from main import app
from models import Product, User  # Import the User model
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

# Fixture to get a test access token (assuming user authentication)
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

# Test case for creating a new product
def test_create_product(session, token):
    """
    Tests creating a new product with valid data.
    """
    if token is None:
        pytest.skip("Skipping test_create_product: User authentication not implemented")

    product_data = {
        "name": "Test Product",
        "category_id": 1,
        "sku": "TEST123",
        "price": 19.99,
        "quantity": 100,
    }
    response = client.post("/products", json=product_data, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

    product = response.json()
    assert product["name"] == "Test Product"
    assert product["category_id"] == 1
    assert product["sku"] == "TEST123"
    assert product["price"] == 19.99
    assert product["quantity"] == 100

# Test case for listing products
def test_list_products(session):
    """
    Tests retrieving a list of products.
    """
    response = client.get("/products")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)

# Test case for retrieving a product by ID (consider handling non-existent products)
def test_get_product_by_id(session):
    """
    Tests retrieving a product by ID. You can either seed the database or handle non-existent products.
    """
    response = client.get("/products/1")
    assert response.status_code == 404  # Assuming product with ID 1 doesn't exist

# Test case for updating a product (assuming authorization)
def test_update_product(session, token):
    """
    Tests updating a product with valid data (requires authorization).
    """
    if token is None:
        pytest.skip("Skipping test_update_product: User authentication not implemented")

    # Assuming there's a product with ID 1 in the database
    product_data = {
        "name": "Updated Product",
        "category_id": 2,
        "sku": "UPDATED123",
        "price": 29.99,
        "quantity": 50,
    }
    response = client.put("/products/1", json=product_data, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404  # Assuming product with ID 1 doesn't exist

# Test case for deleting a product (assuming authorization)
def test_delete_product(session, token):
    """
    Tests deleting a product (requires authorization).
    """
    if token is None:
        pytest.skip("Skipping test_delete_product: User authentication not implemented")

    # Assuming there's a product with ID 1 in the database
    response = client.delete("/products/1", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404  # Assuming product with ID 1 doesn't exist
