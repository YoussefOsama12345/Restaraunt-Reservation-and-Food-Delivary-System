# app/db/database.py
# ---
# UPDATED BY AI: Ensured async database session management, improved compatibility with FastAPI async dependencies, and fixed import issues.
# ---
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Add the parent directory to sys.path to allow absolute imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.db.models.base import Base
from app.settings import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=False)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with async_session() as session:
        yield session
