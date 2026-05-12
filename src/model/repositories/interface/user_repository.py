from abc import ABC, abstractmethod

# ABC as signature implies that whoever inherits this class
# must (mandatory) implement all methods inside it
class UserRepositoryInterface(ABC):
    @abstractmethod
    async def insert_users(self, user_data: dict) -> None: pass

    @abstractmethod
    async def retrieve_users_by_name(self, name: str) -> list[dict]: pass
