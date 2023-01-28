from models.movies import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    def __init__(self,db) -> None:
        self.db =db

    def getmovies(self):
        result = self.db.query(MovieModel).all
        return result

    def getmovie(self,id):
        result = self.db.query(MovieModel).filter(MovieModel.id==id).first()
        return result

    def getmoviebycategory(self,category):
        result = self.db.query(MovieModel).filter(MovieModel.category==category).all()
        return result

    def createmovie(self, movie: Movie):
        newmovie = MovieModel(**movie.dict())
        self.db.add(newmovie)
        self.db.commit()
        return 
    
    def updatemovie(self, id:int, movie:Movie):
        data = self.db.query(MovieModel).filter(MovieModel.id==id).first()
        data.title = movie.title
        data.overview = movie.overview
        data.year = movie.year
        data.rating = movie.rating
        data.category = movie.category
        self.db.commit()
        return 
    
    def deletemovie(self, id:int):
       data = self.db.query(MovieModel).filter(MovieModel.id == id).first()
       self.db.delete(data)
       self.db.commit()
       return