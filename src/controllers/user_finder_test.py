import pytest
from src.controllers.user_finder import UserFinder

class UserRepositoryMock:
    def __init__(self):
        self.retrieve_users_by_name_att = {}

    async def retrieve_users_by_name(self, user_name: str) -> list[dict]:
        self.retrieve_users_by_name_att['user_name'] = user_name
        return [{'user_name': 'faa'}, {'user_name': 'bar'}]
    
@pytest.mark.asyncio
async def test_retrieve_user_by_name():
    user_repository = UserRepositoryMock()
    user_finder = UserFinder(user_repository)
    user_name = 'John doe'

    response = await user_finder.find_user_by_name(user_name)
    assert user_repository.retrieve_users_by_name_att['user_name'] == user_name

    assert response['type'] == 'USERS'
    assert response['count'] == 2
    assert 'attr' in response
    assert isinstance(response['attr'], list)
    assert isinstance(response['attr'][0], dict)