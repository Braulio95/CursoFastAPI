from fastapi import APIRouter
from fastapi import Path, Query, Depends
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.responses import JSONResponse
from config.database import Session
from models.movies import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwtbearer import JWTBearer

movierouter = APIRouter()

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

@movierouter.get('/movies',tags = ['movies'], status_code=200, response_model=List[Movie],dependencies= [Depends(JWTBearer())])
def getmovies()->List[Movie]:
    db = Session()
    data = db.query(MovieModel).all()
    return JSONResponse(status_code=200, content= jsonable_encoder(data))

@movierouter.get('/movies/{id}', tags = ['movies'], response_model=Movie)
def getmovie(id:int = Path(ge =1, le=2000))->Movie:
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={"message":"no encontrado"})
    return JSONResponse(status_code=200, content= jsonable_encoder(data))

@movierouter.get('/movies/', tags = ['movies'],response_model=List[Movie])
def getmoviesbycategory(category:str = Query(min_length=5,max_length=15))->List[Movie]:
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.category == category).all()
    if not data:
        return JSONResponse(status_code=404, content={"message":"no encontrado"})
    return JSONResponse(status_code=200, content= jsonable_encoder(data))
    

@movierouter.post('/movies/',tags = ['movies'], status_code=201, response_model=dict)
def createmovies(movie: Movie)->dict:
    db =Session()
    newmovie = MovieModel(**movie.dict())
    db.add(newmovie)
    db.commit()
    return JSONResponse(status_code=201, content={"mensaje":"se modificó la película"}) 

@movierouter.put('/movies/{id}', tags = ['movies'], response_model=dict, status_code=200)
def updatemovie(id:int, movie: Movie)->dict:
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={"message":"no encontrado"})
    data.title = movie.title
    data.overview = movie.overview
    data.year = movie.year
    data.rating = movie.rating
    data.category = movie.category
    db.commit()
    return JSONResponse(status_code=200, content={"message":"Modificación exitosa"})

@movierouter.delete('/movies/{id}',tags = ['movies'], status_code=200, response_model=dict)
def deletemovie(id:int)->dict:
    db = Session()
    data = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not data:
        return JSONResponse(status_code=404, content={"message":"no encontrado"})
    db.delete(data)
    db.commit()
    return JSONResponse(status_code=200, content={"message":"Película eliminada"})
    