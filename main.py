from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int]= None
    title: str = Field(min_length=5,max_length=15)
    overview: str = Field(min_length=15,max_length=50)
    year: int = Field(le=2024)
    rating: float
    category: str

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

@app.get('/movies',tags = ['movies'])
def getmovies():
    return movies

@app.get('/movies/{id}', tags = ['movies'])
def getmovie(id:int):
    for movie in movies:
        if movie['id']==id:
            return movie

    return [] 

@app.get('/movies/', tags = ['movies'])
def getmoviesbycategory(category:str, year:int):
    for movie in movies:
        if movie['category']==category and movie['year']==year:
            return movie 
    return[]

@app.post('/movies/',tags = ['movies'])
def createmovies(movie: Movie):
    movies.append(movie)
    return movies 

@app.put('/movies/{id}', tags = ['movies'])
def updatemovie(id:int, movie: Movie):
    for movie in movies:
        if movie['id']==id:
            movie['title']=movie.title
            movie['overview']=movie.overview
            movie['year']=movie.year
            movie['rating']=movie.rating
            movie['category']=movie.category
            return movies

@app.delete('/movies/{id}',tags = ['movies'])
def deletemovie(id:int):
    for movie in movies:
        if movie["id"]==id:
            movies.remove(movie)
            return movies
