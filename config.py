from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class DatabaseSettings(BaseSettings):
    """Database connection settings"""
    
    host: str = os.getenv("TEST_DB_HOST")
    port: int = int(os.getenv("TEST_DB_PORT"))
    user: str = os.getenv("TEST_DB_USER")
    password: str = os.getenv("TEST_DB_PASSWORD")
    database: str = os.getenv("TEST_DB_NAME")

db_settings = DatabaseSettings()
