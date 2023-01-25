from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.responses import JSONResponse

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

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

@app.get('/', tags = ['home'])
def message():
    return {'hello':'world'}

@app.get('/movies',tags = ['movies'], status_code=200)
def getmovies():
    return JSONResponse(status_code=200, content=movies)

@app.get('/movies/{id}', tags = ['movies'])
def getmovie(id:int = Path(ge =1, le=2000)):
    for movie in movies:
        if movie['id']==id:
            return JSONResponse(content=movie)

    return JSONResponse(status_code=404,content=[])

@app.get('/movies/', tags = ['movies'])
def getmoviesbycategory(category:str = Query(min_length=5,max_length=15), year:int = Query(ge=1900,le=2023)):
    for movie in movies:
        if movie['category']==category and movie['year']==year:
            return JSONResponse(content=movie) 
    return JSONResponse(content=[])

@app.post('/movies/',tags = ['movies'], status_code=201)
def createmovies(movie: Movie):
    movies.append(movie)
    return JSONResponse(status_code=201, content={"mensaje":"se modificó la película"}) 

@app.put('/movies/{id}', tags = ['movies'])
def updatemovie(id:int, movie: Movie):
    for movie in movies:
        if movie['id']==id:
            movie['title']=movie.title
            movie['overview']=movie.overview
            movie['year']=movie.year
            movie['rating']=movie.rating
            movie['category']=movie.category
            return JSONResponse(content={"mensaje":"se modificó la película"})

@app.delete('/movies/{id}',tags = ['movies'], status_code=200)
def deletemovie(id:int):
    for movie in movies:
        if movie["id"]==id:
            movies.remove(movie)
            return JSONResponse(status_code=200, content={"mensaje":"se eliminó la película"})
