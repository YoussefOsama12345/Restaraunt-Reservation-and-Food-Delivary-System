"""
main.py

FastAPI application entry point for the Restaurant Management System (RMS).
Includes all API routers and sets up middleware, docs, and versioning.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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

# Initialize FastAPI app
app = FastAPI(
    title="Restaurant Management System API",
    version="1.0.0",
    description="API for managing restaurants, orders, users, deliveries, and more.",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers with prefixes
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(address_router, prefix="/api/addresses", tags=["Addresses"])
app.include_router(restaurant_router, prefix="/api/restaurants", tags=["Restaurants"])
app.include_router(category_router, prefix="/api/categories", tags=["Categories"])
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

# Health check route

