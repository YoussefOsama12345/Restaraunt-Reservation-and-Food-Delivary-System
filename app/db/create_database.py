# app/db/create_database.py
# ---
# UPDATED BY AI: Improved database creation script for async compatibility and error handling. Ensured it matches project DB config.
# ---
import asyncio
import aiomysql
from app.settings import settings

async def create_database():
    """
    Create the database if it doesn't exist.
    """
    # Connect to MySQL without specifying a database
    conn = await aiomysql.connect(
        host=settings.DB_HOST,
        port=int(settings.DB_PORT),
        user=settings.DB_USER,
        password=settings.DB_PASSWORD
    )
    
    try:
        async with conn.cursor() as cursor:
            # Create database if it doesn't exist
            await cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME}")
            print(f"Database '{settings.DB_NAME}' created or already exists.")
    finally:
        conn.close()
        await conn.wait_closed()

if __name__ == "__main__":
    asyncio.run(create_database()) 