from app.db import session_factory
from app.repository.users import UserRepository
from app.schemas.users import UserSchemaRequest


async def create_user_facade(user: UserSchemaRequest):
    with session_factory() as session:
        user_repository = UserRepository(session)
        # hash user password

        new_user = user_repository.create_user(user.dict())
        return new_user
