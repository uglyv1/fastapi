from src.model.repositories.interface.user_repository import UserRepositoryInterface
from src.controllers.interface.user_register import UserRegisterInterface


# typing the user_repository with the interface takes part on the
# DI dependency injection (SOLID)
class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    # while there is only a pass inside the function
    # there's no need to type its return but with None
    # which makes sense, afterwards the typing should be replaced by
    # the expected type
    async def register_user(self, user_data: dict) -> dict:
        self.__validate_user_data(user_data)
        await self.__registry_user(user_data)
        return self.__format_response(user_data)

    # after defining this method entirely,
    # we replace the pass from register_user by the
    # validate_user_data method
    # NO ASYNC HERE SINCE WE ARE TREATING A STATIC DATA
    def __validate_user_data(self, user_data: dict) -> None:
        age = user_data['age']
        uf = user_data['uf']

        if uf not in ['MG', 'BA', 'CE', 'SC']:
            raise Exception('Invalid State')

        if age < 0 or age > 120:
            raise Exception('Invalid age')
        
    async def  __registry_user(self, user_data: dict) -> None:
        await self.__user_repository.insert_users(user_data)

    def __format_response(self, user_data: dict) -> dict:
        return {
            'type': 'USERS',
            'count': 1,
            'attr': user_data
        }
