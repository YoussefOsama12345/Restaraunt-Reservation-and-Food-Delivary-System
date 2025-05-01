"""
app/core/settings.py

Centralized configuration management using environment variables.
This module loads database credentials and other sensitive config using python-dotenv.

Usage:
    from app.core.settings import settings
    engine = create_async_engine(settings.DATABASE_URL)

Environment Variables Expected:
    - DB_USER
    - DB_PASSWORD
    - DB_HOST
    - DB_PORT
    - DB_NAME
    - SECRET_KEY
    - DATABASE_URL
"""

from dotenv import load_dotenv
import os
# Load .env from the project root, regardless of where the script is run
load_dotenv(dotenv_path=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env')), override=True)

class Settings:
    """
    Application settings loaded from environment variables.

    Attributes:
        DB_USER (str): MySQL database username
        DB_PASSWORD (str): MySQL database password
        DB_HOST (str): Host where MySQL is running
        DB_PORT (str): Port for MySQL server
        DB_NAME (str): Target database name
        SECRET_KEY (str): Secret key for JWT token generation
    """

    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    SECRET_KEY: str = os.getenv("SECRET_KEY")  

settings = Settings()

# Use DATABASE_URL only from environment, outside the class
DATABASE_URL = os.getenv("DATABASE_URL")

# Debug print to confirm .env loading
# print("DEBUG: DATABASE_URL from .env:", DATABASE_URL)

if __name__ == "__main__":
    pass