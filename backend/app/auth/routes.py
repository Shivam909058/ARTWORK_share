# backend/app/auth/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import UserCreate, ArtworkCreate
from app.crud import create_user, create_artwork

auth_router = APIRouter()

@auth_router.post("/signup/")
async def sign_up(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)

@auth_router.post("/artworks/")
async def upload_artwork(artwork: ArtworkCreate, artist_id: int, db: AsyncSession = Depends(get_db)):
    return await create_artwork(db, artwork, artist_id)
