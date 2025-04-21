"""
Fixtures for automated tests.

This module defines reusable pytest fixtures for unit, integration, and API tests.
Fixtures are used to set up common test prerequisites like:

- Database session (rollback-safe)
- FastAPI test client
- Mock users (regular and admin)
- Auth tokens (JWT or Firebase)
- Sample payloads for schemas (e.g., menu items, orders, reservations)
- Pre-seeded data for controllers/services

These fixtures improve test isolation, reduce redundancy, and ensure a clean test environment.

Usage:
    Import the required fixture(s) in your test modules:
    
        def test_example(client, db_session, sample_user):
            ...

Pytest will automatically detect and inject them when needed.
"""
