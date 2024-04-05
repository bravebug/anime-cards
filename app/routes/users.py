from fastapi import APIRouter

from app.facade.users import create_user_facade
from app.schemas.users import UserSchemaResponse, UserSchemaRequest

user_router = APIRouter()

@user_router.post('/users', response_model=UserSchemaResponse, status_code=201, )
def create_user(user: UserSchemaRequest):
    new_user = create_user_facade(user)
    return new_user
