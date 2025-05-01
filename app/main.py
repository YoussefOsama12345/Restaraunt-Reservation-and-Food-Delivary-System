"""
main.py

FastAPI application entry point for the Restaurant Management System (RMS).
Includes all API routers and sets up middleware, docs, and versioning.
"""
# ---
# UPDATED BY AI: Ensured all routers use async endpoints, fixed import issues, and improved startup/shutdown event handling for FastAPI best practices.
# ---
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.db.models.menu_item import MenuItem
import os
from sqlalchemy import select
from app.settings import settings, DATABASE_URL
import logging
import logging.config

# Use logging.ini to control SQLAlchemy and all logging output
logging_ini_path = os.path.join(os.path.dirname(__file__), 'logging.ini')
if os.path.exists(logging_ini_path):
    logging.config.fileConfig(logging_ini_path, disable_existing_loggers=False)

# Optionally suppress custom startup prints for a cleaner console
SHOW_STARTUP_PRINTS = False

from app.api.routes.users import router as user_router
from app.api.routes.addresses import router as address_router
from app.api.routes.restaurants import router as restaurant_router
from app.api.routes.categories import router as category_router
from app.api.routes.menu_items import router as menu_item_router
from app.api.routes.cart import router as cart_router
from app.api.routes.orders import router as order_router
from app.api.routes.payments import router as payment_router
from app.api.routes.reservations import router as reservation_router
from app.api.routes.reviews import router as review_router
from app.api.routes.deliveries import router as delivery_task_router
from app.api.routes.notifications import router as notification_router
from app.api.routes.support import router as support_ticket_router
from app.api.routes.inventory import router as inventory_router
from app.api.routes.auth import router as auth_router
from app.api.routes.order_item import router as order_item_router

# Import middleware components
# Note: Custom middleware for handling SQLAlchemy errors has been removed

# Initialize FastAPI app
app = FastAPI(
    title="Restaurant Management System API",
    version="1.0.0",
    description="API for managing restaurants, orders, users, deliveries, and more.",
)

# Add HTTPBearer security scheme to OpenAPI docs
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "HTTPBearer": {
            "type": "http",
            "scheme": "bearer"
        }
    }
    # Apply HTTPBearer globally
    for path in openapi_schema["paths"].values():
        for op in path.values():
            op["security"] = [{"HTTPBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Use the dynamically built DATABASE_URL from settings
engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

@app.on_event("startup")
async def log_menu_items_and_db():
    if SHOW_STARTUP_PRINTS:
        print(f"[Startup] Using DATABASE_URL: {DATABASE_URL}")
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(MenuItem).limit(5))
        items = result.scalars().all()
        if SHOW_STARTUP_PRINTS:
            print("[Startup] First 5 menu items in DB:")
            for item in items:
                print(f"ID: {item.id}, Name: {item.name}, Price: {item.price}")

# Configure middleware
# Note: Using direct error handling in controllers instead of middleware

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers with prefixes
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(address_router, prefix="/addresses", tags=["Addresses"])
app.include_router(restaurant_router, prefix="/api/restaurants", tags=["Restaurants"])
app.include_router(category_router, prefix="/categories", tags=["Categories"])
app.include_router(menu_item_router, prefix="/api/menu-items", tags=["Menu Items"])
app.include_router(cart_router, prefix="/api/cart", tags=["Cart"])
app.include_router(order_router, prefix="/api/orders", tags=["Orders"])
app.include_router(payment_router, prefix="/api/payments", tags=["Payments"])
app.include_router(reservation_router, prefix="/api/reservations", tags=["Reservations"])
app.include_router(review_router, prefix="/api/reviews", tags=["Reviews"])
app.include_router(delivery_task_router, prefix="/api/deliveries", tags=["Delivery Tasks"])
app.include_router(notification_router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(support_ticket_router, prefix="/api/support", tags=["Support Tickets"])
app.include_router(inventory_router, prefix="/api/inventory", tags=["Inventory"])
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(order_item_router, prefix="/order-items", tags=["Order Items"])
# Health check route
