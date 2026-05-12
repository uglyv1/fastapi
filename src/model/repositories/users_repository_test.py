import pytest
from src.model.repositories.users_repository import UsersRepository

@pytest.mark.asyncio
@pytest.mark.skip(reason='database insertion')
async def test_insert_user():
    new_user = {
        'user_name': 'testuser',
        'age': 30,
        'uf': 'sp'    
    }

    repo = UsersRepository()
    await repo.insert_users(new_user)

@pytest.mark.asyncio
async def test_retrieve_users_by_name():
    repo = UsersRepository()
    response = await repo.retrieve_users_by_name('testuser')
    print(f' FOI - {response}')