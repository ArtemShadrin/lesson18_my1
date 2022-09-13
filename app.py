# app.py
from flask_restx import Api, Resource
from config import app, db
from models import Movie, Director, Genre
from schemas import MovieSchema, DirectorSchema, GenreSchema
from flask import request

api = Api(app)  # создаем API

movie_ns = api.namespace('movies')  # регистрируем namespaces
director_ns = api.namespace('directors')
genre_ns = api.namespace('genres')


### route movies ###
@movie_ns.route('/')
class MoviesViews(Resource):
    # def get(self):
    #     movies_schema = MovieSchema(many=True)
    #     all_movies = db.session.query(Movie).all()
    #     return  movies_schema.dump(all_movies), 200
    #     return MovieSchema(many=True).dump(Movie.query.all()), 200

    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        query = Movie.query
        if director_id:
            query = query.filter(director_id == Movie.director_id)
        if genre_id:
            query = query.filter(genre_id == Movie.genre_id)
        return MovieSchema(many=True).dump(query.all()), 200

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)
        with db.session.begin():
            db.session.add(new_movie)
        return '', 201


@movie_ns.route('/<int:mid>')
class MoviesViews(Resource):
    def get(self, mid: int):  # получение данных
        try:
            movies_schema = MovieSchema()
            movie = db.session.query(Movie).filter(Movie.id == mid).one()
            return movies_schema.dump(movie), 200
            # return MovieSchema().dump(Movie.query.get(id))
        except Exception as e:
            return str(e), 404

    def put(self, mid: int):  # замена данных
        movie = db.session.query(Movie).get(mid)
        req_json = request.json

        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")

        db.session.add(movie)
        db.session.commit()

        return '', 204

    def patch(self, mid: int):  # частичное обновление данных
        movie = db.session.query(Movie).get(mid)
        req_json = request.json

        if "title" in req_json:
            movie.title = req_json.get("title")
        if "description" in req_json:
            movie.title = req_json.get("description")
        if "trailer" in req_json:
            movie.title = req_json.get("trailer")
        if "year" in req_json:
            movie.title = req_json.get("year")
        if "rating" in req_json:
            movie.title = req_json.get("rating")
        if "genre_id" in req_json:
            movie.title = req_json.get("genre_id")
        if "director_id" in req_json:
            movie.title = req_json.get("director_id")

        db.session.add(movie)
        db.session.commit()

        return '', 204

    def delete(self, mid: int):
        movie = db.session.query(Movie).get(mid)

        db.session.delete(movie)
        db.session.commit()

        return '', 204

### route directors ###
@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        directors_schema = DirectorSchema(many=True)
        all_directors = db.session.query(Director).all()
        return directors_schema.dump(all_directors), 200
        # return DirectorSchema(many=True).dump(Director.query.all()), 200

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)
        with db.session.begin():
            db.session.add(new_director)
        return '', 201


@director_ns.route('/<int:did>')
class DirectorsViews(Resource):
    def get(self, did: int):  # получение данных
        try:
            directors_schema = DirectorSchema()
            director = db.session.query(Director).filter(Director.id == did).one()
            return directors_schema.dump(director), 200
            # return MovieSchema().dump(Movie.query.get(id))
        except Exception as e:
            return str(e), 404

    def put(self, did: int):  # замена данных
        director = db.session.query(Director).get(did)
        req_json = request.json

        director.name = req_json.get("name")

        db.session.add(director)
        db.session.commit()

        return '', 204

    def patch(self, mid: int):  # частичное обновление данных
        director = db.session.query(Director).get(mid)
        req_json = request.json

        if "name" in req_json:
            director.name = req_json.get("name")

        db.session.add(director)
        db.session.commit()

        return '', 204

    def delete(self, did: int):
        director = db.session.query(Director).get(did)

        db.session.delete(director)
        db.session.commit()

        return '', 204

### route genres ###
@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        genres_schema = GenreSchema(many=True)
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres), 200
        # return GenreSchema(many=True).dump(Genre.query.all()), 200

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)
        with db.session.begin():
            db.session.add(new_genre)
        return '', 201


@genre_ns.route('/<int:gid>')
class GenresViews(Resource):
    def get(self, gid: int):  # получение данных
        try:
            genres_schema = GenreSchema()
            genre = db.session.query(Genre).filter(Genre.id == gid).one()
            return genres_schema.dump(genre), 200
            # return GenresSchema().dump(Genres.query.get(id))
        except Exception as e:
            return str(e), 404

    def put(self, gid: int):  # замена данных
        genre = db.session.query(Genre).get(gid)
        req_json = request.json

        genre.name = req_json.get("name")

        db.session.add(genre)
        db.session.commit()

        return '', 204

    def patch(self, mid: int):  # частичное обновление данных
        genre = db.session.query(Genre).get(mid)
        req_json = request.json

        if "name" in req_json:
            genre.name = req_json.get("name")

        db.session.add(genre)
        db.session.commit()

        return '', 204

    def delete(self, gid: int):
        genre = db.session.query(Genre).get(gid)

        db.session.delete(genre)
        db.session.commit()

        return '', 204


if __name__ == '__main__':
    app.run(debug=True)
