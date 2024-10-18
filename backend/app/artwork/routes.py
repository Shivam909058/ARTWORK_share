from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import UserCreate
from app.crud import create_user

auth_router = APIRouter()

@auth_router.post("/signup/")
def sign_up(user: UserCreate, db: Session = Depends(SessionLocal)):
    return create_user(db, user)
