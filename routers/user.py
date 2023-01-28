from fastapi import APIRouter
from jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User

userrouter = APIRouter()


@userrouter.post('/login',tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token:str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)