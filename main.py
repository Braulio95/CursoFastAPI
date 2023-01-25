from fastapi import FastAPI

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

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
def createmovies(id:int, title:str, overview:str, year:int, rating:float, category:str):
    movies.append({
        "id": id,
		"title": title,
		"overview": overview,
		"year": year,
		"rating": rating,
		"category": category

    })
    return movies 

@app.put('/movies/{id}', tags = ['movies'])
def updatemovie(id:int, title:str, overview:str, year:int, rating:float, category:str):
    for movie in movies:
        if movie['id']==id:
            movie['title']=title
            movie['overview']=overview
            movie['year']=year
            movie['rating']=rating
            movie['category']=category
            return movies

@app.delete('/movies/{id}',tags = ['movies'])
def deletemovie(id:int):
    for movie in movies:
        if movie["id"]==id:
            movies.remove(movie)
            return movies
