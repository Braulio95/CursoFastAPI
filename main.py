from fastapi import FastAPI
from config.database import engine, Base
from middlewares.errorhandler import ErrorHandler
from routers.movie import movierouter
from routers.user import userrouter

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movierouter)
app.include_router(userrouter)
Base.metadata.create_all(bind=engine)



""""
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
"""
Primer ejemplo para probar de forma sencilla el método get y regresar un mensaje de hola mundo en formato JSON

@app.get('/', tags = ['home'])
def message():
    return {'hello':'world'}
"""

""" Función para logear a un usuario con correo y contraseña"""



