# backend/app/crud.py
from sqlalchemy.future import select
from app.models import User, Artwork  # Ensure you have User and Artwork models
from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def create_artwork(db: AsyncSession, artwork: ArtworkCreate, artist_id: int):
    db_artwork = Artwork(**artwork.dict(), artist_id=artist_id)
    db.add(db_artwork)
    await db.commit()
    await db.refresh(db_artwork)
    return db_artwork
