from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from models import Category, Product
from pydantic import BaseModel

import auth
from models import Product as ProductSchema, Category as CategorySchema, User
from auth import create_access_token, get_current_user_from_token, hash_password, verify_password
from database import get_db, create_product, get_products, get_product_by_id, update_product, delete_product, \
    create_category, get_categories, get_category_by_id, update_category, delete_category

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

# Dependency to get current user from token
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    user = get_current_user_from_token(db, token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/products", response_model=List[ProductSchema])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    return products

@app.post("/products", response_model=ProductSchema)
def create_new_product(product: ProductSchema, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_product = create_product(db, Product(**product.dict()))
    return db_product

@app.get("/products/{product_id}", response_model=ProductSchema)
def retrieve_product(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=ProductSchema)
def update_existing_product(product_id: int, product: ProductSchema, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    updated_product = update_product(db, product_id, Product(**product.dict()))
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@app.delete("/products/{product_id}", response_model=ProductSchema)
def delete_existing_product(product_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    deleted_product = delete_product(db, product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product

@app.get("/categories", response_model=List[CategorySchema])
def list_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = get_categories(db, skip=skip, limit=limit)
    return categories

@app.post("/categories", response_model=CategorySchema)
def create_new_category(category: CategorySchema, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_category = create_category(db, Category(**category.dict()))
    return db_category

@app.get("/categories/{category_id}", response_model=CategorySchema)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = get_category_by_id(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.put("/categories/{category_id}", response_model=CategorySchema)
def update_existing_category(category_id: int, category: CategorySchema, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    updated_category = update_category(db, category_id, Category(**category.dict()))
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@app.delete("/categories/{category_id}", response_model=CategorySchema)
def delete_existing_category(category_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    deleted_category = delete_category(db, category_id)
    if deleted_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
