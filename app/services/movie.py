from app.dao.models.movie import Movie
from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        pass

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')
        movie = self.session.query(Movie).get(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get('id')
        movie = self.session.query(Movie).get(mid)

        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.title = data.get("description")
        if "trailer" in data:
            movie.title = data.get("trailer")
        if "year" in data:
            movie.title = data.get("year")
        if "rating" in data:
            movie.title = data.get("rating")
        if "genre_id" in data:
            movie.title = data.get("genre_id")
        if "director_id" in data:
            movie.title = data.get("director_id")

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)