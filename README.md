
```markdown
# FastAPI Electronics Catalog API 📚

Welcome to the Electronics Catalog API! This project is a simple REST API for managing an electronics store's inventory, built with Python's FastAPI framework. It includes functionalities for listing, retrieving, creating, updating, and deleting products, with JWT authentication for secure operations.

## 📑 Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Seeding the Database](#seeding-the-database)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [Contact](#contact)

## 💡 Introduction

Your local electronics store has started to expand, but track their entire inventory by hand. They have asked you to build a simple cataloging system as a REST API so that they can integrate with mobile and desktop applications in the future.

### Requirements
The API should be able to:
- List all products
- List all categories
- Retrieve a single product
- Create a product
- Update a product
- Delete a product

### Authentication
- Only authenticated users can create, update, or delete a product.
- No authentication is required to retrieve or list products and categories.

### Data
All entities should have timestamp fields (created_at, and modified_at).

#### Products
- Name
- Category
- SKU
- Price
- Quantity

#### Categories
- Name

## 🏗️ Project Structure

Here's an overview of the project's structure:

```plaintext
.
├── .env
├── config.py
├── database.py
├── models.py
├── auth.py
├── main.py
├── tests
│   ├── test_categories.py
│   └── test_products.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

### 🗂️ Detailed Overview

| File/Directory            | Description                                                                |
|---------------------------|----------------------------------------------------------------------------|
| **.env**                  | Contains environment variables.                                            |
| **config.py**             | Application configuration.                                                 |
| **database.py**           | Database connection management.                                            |
| **models.py**             | Data models/schema definitions.                                            |
| **auth.py**               | Authentication functionality.                                              |
| **main.py**               | Entry point of the application.                                            |
| **tests/**                | Contains test cases.                                                       |
| ├── **test_categories.py**| Tests for category functionalities.                                         |
| └── **test_products.py**  | Tests for product functionalities.                                         |
| **Dockerfile**            | Instructions to build the Docker image.                                    |
| **docker-compose.yml**    | Define and run multi-container Docker applications.                        |
| **requirements.txt**      | Project dependencies.                                                      |

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nikhil-707/FastAPI-Electronics-Catalog-REST-API.git
   cd FastAPI-Electronics-Catalog-REST-API

   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables in the `.env` file.

## 🚀 Running the Application

Run the FastAPI development server:
```bash
uvicorn main:app --reload
```

## 🧪 Running Tests

Execute the test cases using pytest:
```bash
python -m pytest test_categories.py
python -m pytest test_products.py
```

## 🐳 Docker Setup

1. Build the Docker image:
   ```bash
   docker-compose build 
   ```

2. Run the application using Docker Compose:
   ```bash
   docker-compose up
   ```


```
