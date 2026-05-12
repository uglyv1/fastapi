# pylint:disable = w212 
from sqlalchemy import insert, select
from src.model.entities.users import user
from src.model.settings.database_connection_handler import DatabaseConnectionHandler
from .interface.user_repository import UserRepositoryInterface

# passing the userrepositoryinterface in the method signature
# obliges the class to implement all its methods
class UsersRepository(UserRepositoryInterface):
    async def insert_users(self, user_data: dict) -> None:
        async with DatabaseConnectionHandler() as db_handler:
            query = insert(user).values(**user_data)
            await db_handler.session.execute(query)
            await db_handler.session.commit()

    async def retrieve_users_by_name(self, name: str) -> list[dict]:
        async with DatabaseConnectionHandler() as db_handler:
            query = (
                select(user)
                .where(user.c.user_name == name)
            )

        result = await db_handler.session.execute(query)
        rows = result.fetchall()

        users_list = [dict(row._mapping) for row in rows]
        return users_list