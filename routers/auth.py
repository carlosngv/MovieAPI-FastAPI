
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemes.user import User
from utils.jwt_manager import create_token

auth_router = APIRouter()

@auth_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == 'admin@mail.com' and user.password == 'admin':
        token: str = create_token(user.dict())
    return JSONResponse(status_code=200, content={'msg': 'Login éxitoso', 'token': token})
