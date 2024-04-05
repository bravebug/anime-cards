

from typing import List

from sqlalchemy import insert
from sqlalchemy.orm import Session

from app.models.users import Users
from app.schemas.users import UserSchemaResponse
from app.db import engine, session_factory


class UserRepository:
    """
    Repository class for handling user-related operations in the database.
    """

    def __init__(self, session: Session):
        """
        Initializes a new instance of the UserRepository class.

        :param session: SQLAlchemy session object.
        """
        self.session = session

    def create_user(self, user_data):
        """
        Creates a new user in the database using SQLAlchemy query builder and returns a UserSchemaResponse object.

        :param user_data: A dictionary containing user data.
        :return: A UserSchemaResponse object representing the created user.
        """
        user = insert(Users).values(**user_data)
        result = self.session.execute(user)
        user_data['id'] = result.inserted_primary_key[0]
        user_schema = UserSchemaResponse(**user_data)
        return user_schema
