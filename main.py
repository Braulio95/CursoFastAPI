from fastapi import FastAPI, Path, Query, Request, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.responses import JSONResponse
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales inválidas")



class User(BaseModel):
    email:str
    password:str


class Movie(BaseModel):
    id: Optional[int]= None
    title: str = Field(min_length=5,max_length=15)
    overview: str = Field(min_length=15,max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(le=10, ge=1)
    category: str = Field(min_length=5,max_length=15)

    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "title":"Mí película",
                "overview":"Mi descripción",
                "year":2022,
                "rating":8.0,
                "category":"Acción"
            }
        }


movies = [
      {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": 2009,
		"rating": 7.8,
		"category": "Acción"
	},
         {
		"id": 2,
		"title": "El padrino",
		"overview": "Relato de la familia Corleone ...",
		"year": 1973,
		"rating": 9.8,
		"category": "Drama"
	},
        {
        "id": 3,
        "title": "Star Wars",
        "overview": "Reseña star wars",
        "year": 1977,
        "rating": 8.5,
        "category": "Acción"
    }

]

"""
Primer ejemplo para probar de forma sencilla el método get y regresar un mensaje de hola mundo en formato JSON

@app.get('/', tags = ['home'])
def message():
    return {'hello':'world'}
"""

""" Función para logear a un usuario con correo y contraseña"""
@app.post('/login',tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token:str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)


@app.get('/movies',tags = ['movies'], status_code=200, response_model=List[Movie], dependencies= [Depends(JWTBearer)])
def getmovies()->List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get('/movies/{id}', tags = ['movies'], response_model=Movie)
def getmovie(id:int = Path(ge =1, le=2000))->Movie:
    for movie in movies:
        if movie['id']==id:
            return JSONResponse(content=movie)

    return JSONResponse(status_code=404,content=[])

@app.get('/movies/', tags = ['movies'],response_model=List[Movie])
def getmoviesbycategory(category:str = Query(min_length=5,max_length=15), year:int = Query(ge=1900,le=2023))->List[Movie]:
    for movie in movies:
        if movie['category']==category and movie['year']==year:
            return JSONResponse(content=movie) 
    return JSONResponse(content=[])

@app.post('/movies/',tags = ['movies'], status_code=201, response_model=dict)
def createmovies(movie: Movie)->dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={"mensaje":"se modificó la película"}) 

@app.put('/movies/{id}', tags = ['movies'], response_model=dict, status_code=200)
def updatemovie(id:int, movie: Movie)->dict:
    for movie in movies:
        if movie['id']==id:
            movie['title']=movie.title
            movie['overview']=movie.overview
            movie['year']=movie.year
            movie['rating']=movie.rating
            movie['category']=movie.category
            return JSONResponse(status_code=200,content={"mensaje":"se modificó la película"})

@app.delete('/movies/{id}',tags = ['movies'], status_code=200, response_model=dict)
def deletemovie(id:int)->dict:
    for movie in movies:
        if movie["id"]==id:
            movies.remove(movie)
            return JSONResponse(status_code=200, content={"mensaje":"se eliminó la película"})
