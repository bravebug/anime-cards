from typing import List

from fastapi import APIRouter
from sqlalchemy import select

from app.db import session_factory
from app.models.characters import Characters
from app.schemas.characters import CharacterSchema

character_router = APIRouter()

@character_router.get(
    '/characters',
    response_model=List[CharacterSchema],
)
def get_characters():
    with session_factory() as session:
        query = select(Characters)
        data = session.execute(query)
        return data.scalars().all()


