from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.security.jwt import decode_access_token
from app.db.database import get_db
from app.db.models.user import User

# Replace OAuth2 or custom auth logic with HTTPBearer
bearer_scheme = HTTPBearer()

# Remove duplicate get_current_user to avoid confusion and ensure only one version is used everywhere