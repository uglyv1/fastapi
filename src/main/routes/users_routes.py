from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=['users'])

@users_routes.post('/users')
async def create_user():
    return JSONResponse(
        content={"hello": "hello world"},
        status_code=200
    )
