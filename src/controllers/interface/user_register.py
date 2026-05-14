from abc import ABC, abstractmethod

class UserRegisterInterface(ABC):
    # notice how we do not need the class constructor inside the interface ..
    # only the method signature
    # def __init__(self, user_repository: UserRepositoryInterface) -> None:
    #     self.__user_repository = user_repository
    @abstractmethod
    async def register_user(self, user_data: dict) -> dict: pass