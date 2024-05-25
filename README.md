
```markdown
# FastAPI Application 🚀

Welcome to the FastAPI application! This project provides a robust foundation for building a modern web application with FastAPI, including database interaction, authentication, and testing.

## 📑 Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [Contact](#contact)

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
   docker build -t fastapi-app .
   ```

2. Run the application using Docker Compose:
   ```bash
   docker-compose up
   ```


```
