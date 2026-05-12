import pytest
from src.controllers.user_register import UserRegister

class UserRepositoryMock:
    def __init__(self):
        self.insert_users_att = {}

    async def insert_users(self, user_data: dict):
        self.insert_users_att['user_data'] = user_data

@pytest.mark.asyncio
async def test_register_user_error_uf():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_user_data = {
        'user_name': 'foo',
        'age': 32,
        'uf' : 'PA' 
    }

    with pytest.raises(Exception) as excinfo:
        await user_register.register_user(invalid_user_data)

    assert str(excinfo.value) == 'Invalid State'
    assert user_repository.insert_users_att == {}

@pytest.mark.asyncio
async def test_register_user_error_age():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    invalid_user_data = {
        'user_name': 'foo',
        'age': -21,
        'uf' : 'MG' 
    }

    with pytest.raises(Exception) as excinfo:
        await user_register.register_user(invalid_user_data)

    assert str(excinfo.value) == 'Invalid age'
    # the not can be used as something more concise, but
    # comparing with a empty dict/obj is semiotic
    # assert not user_repository.insert_users_att == {}
    assert user_repository.insert_users_att == {}