"""Endpoints related to the current user."""

from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse
from app.services.tickets import retrieve_user
from sqlalchemy.orm import Session
from app.db.session import get_db


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    """Return the profile belonging to the bearer token."""

    return current_user


@router.get("/{user_id}")
def get_user(user_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db))->UserResponse:
    return retrieve_user(user_id,current_user,db)
