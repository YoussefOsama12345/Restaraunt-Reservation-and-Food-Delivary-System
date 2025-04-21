# app/db/create_tables.py

import asyncio
import sys
import os

# Add the parent directory to sys.path to allow absolute imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Import the engine and Base class
from app.db.database import engine
from app.db.models.base import Base


async def create_all_tables():
    """
    Create all database tables asynchronously using SQLAlchemy's metadata.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("All tables created successfully.")

if __name__ == "__main__":
    asyncio.run(create_all_tables())
