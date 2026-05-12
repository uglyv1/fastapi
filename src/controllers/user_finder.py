from src.model.repositories.interface.user_repository import UserRepositoryInterface

# typing the user_repository with the interface takes part on the
# DI dependency injection (SOLID)
class UserFinder:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    async def find_user_by_name(self, user_name: str) -> dict:
        users = await self.__user_repository.retrieve_users_by_name(user_name)
        # the attr here matches the users type -> in this case list of dicts
        return {
            'type': 'USERS',
            'count': len(users),
            'attr': users
        }