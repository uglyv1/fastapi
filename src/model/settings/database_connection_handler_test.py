import pytest
from src.model.settings.database_connection_handler import DatabaseConnectionHandler

@pytest.mark.asyncio
@pytest.mark.skip(reason="Requires a real database connection")
async def test_database_connection():
    async with DatabaseConnectionHandler() as database_handler:
        assert database_handler.session is not None