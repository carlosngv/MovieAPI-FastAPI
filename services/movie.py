
from models.movie import MovieTable
from schemes.movie import Movie
class MovieService:
    def __init__(self, db):
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieTable).all()
        return result

    def get_movie(self, id):
        result = self.db.query(MovieTable).filter(MovieTable.id == id).first()
        return result

    def get_movie_by_category(self, category):
        result = self.db.query(MovieTable).filter(MovieTable.category == category).first()
        return result

    def create_movie(self, movie: Movie):
        new_movie = MovieTable(** movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()

    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieTable).filter(MovieTable.id == id).first()
        if not movie:
                return False

        movie.title = data.title
        movie.overview = data.overview
        movie.rating = data.rating
        movie.category = data.category
        movie.year = data.year
        self.db.commit()

        return True
    def delete_movie(self, id):
        result = self.db.query(MovieTable).filter(MovieTable.id == id).first()
        if not result:
            return False
        self.db.delete(result)
        self.db.commit()
        return True
