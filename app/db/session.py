# app/db/session.py
# ---
# Created for synchronous database operations
# ---
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Add the parent directory to sys.path to allow absolute imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.settings import DATABASE_URL

# Create synchronous engine and session factory
# Convert async URL to sync URL by removing the +asyncmy part
sync_database_url = DATABASE_URL.replace('+asyncmy', '')
sync_engine = create_engine(sync_database_url, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=sync_engine)
