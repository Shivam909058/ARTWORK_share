# backend/app/schemas.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class ArtworkBase(BaseModel):
    title: str
    description: str
    file_url: str
    price: float

class ArtworkCreate(ArtworkBase):
    pass

class Artwork(ArtworkBase):
    id: int
    artist_id: int

    class Config:
        orm_mode = True
