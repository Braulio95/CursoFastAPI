from fastapi import APIRouter
from fastapi import Path, Query, Depends
from typing import List
from fastapi.responses import JSONResponse
from config.database import Session
from models.movies import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwtbearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movierouter = APIRouter()



@movierouter.get('/movies',tags = ['movies'], status_code=200, response_model=List[Movie],dependencies= [Depends(JWTBearer())])
def getmovies()->List[Movie]:
    db = Session()
    data = MovieService(db).getmovies()
    return JSONResponse(status_code=200, content= jsonable_encoder(data))

@movierouter.get('/movies/{id}', tags = ['movies'], response_model=Movie)
def getmovie(id:int = Path(ge =1, le=2000))->Movie:
    db = Session()
    data = MovieService(db).getmovie(id)
    if not data:
        return JSONResponse(status_code=404, content={"message":"no encontrado"})
    return JSONResponse(status_code=200, content= jsonable_encoder(data))

@movierouter.get('/movies/', tags = ['movies'],response_model=List[Movie])
def getmoviesbycategory(category:str = Query(min_length=5,max_length=15))->List[Movie]:
    db = Session()
    data = MovieService(db).getmoviebycategory(category)
    if not data:
        return JSONResponse(status_code=404, content={"message":"no encontrado"})
    return JSONResponse(status_code=200, content= jsonable_encoder(data))
    

@movierouter.post('/movies/',tags = ['movies'], status_code=201, response_model=dict)
def createmovies(movie: Movie)->dict:
    db =Session()
    MovieService(db).createmovie(movie)
    return JSONResponse(status_code=201, content={"mensaje":"se modificó la película"}) 

@movierouter.put('/movies/{id}', tags = ['movies'], response_model=dict, status_code=200)
def updatemovie(id:int, movie: Movie)->dict:
    db = Session()
    data = MovieService(db).getmovie(id)
    if not data:
        return JSONResponse(status_code=404, content={"message":"no encontrado"})
    MovieService(db).updatemovie(id,movie)
    return JSONResponse(status_code=200, content={"message":"Modificación exitosa"})

@movierouter.delete('/movies/{id}',tags = ['movies'], status_code=200, response_model=dict)
def deletemovie(id:int)->dict:
    db = Session()
    data = MovieService(db).getmovie(id)
    if not data:
        return JSONResponse(status_code=404, content={"message":"no encontrado"})
    MovieService(db).deletemovie(id)
    return JSONResponse(status_code=200, content={"message":"Película eliminada"})
    