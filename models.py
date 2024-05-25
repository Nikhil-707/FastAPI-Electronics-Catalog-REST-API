from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

class Category(BaseModel):
    id: int
    name: str = Field(..., description="Name of the product category")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of category creation")
    modified_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of category modification")

    class Config:
        from_attributes = True

class Product(BaseModel):
    id: int
    name: str = Field(..., description="Name of the product")
    category_id: int
    sku: str = Field(..., description="Stock Keeping Unit (unique product identifier)")
    price: float = Field(..., gt=0, description="Price of the product (must be positive)")
    quantity: int = Field(..., ge=0, description="Quantity of the product in stock (must be non-negative)")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of product creation")
    modified_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of product modification")

    class Config:
        from_attributes = True

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of user creation")
