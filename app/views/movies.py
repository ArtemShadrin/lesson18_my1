from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.models.movie import Movie, MovieSchema

movie_ns = Namespace('movies')

movies_schema = MovieSchema()


@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        query = Movie.query
        if director_id:
            query = query.filter(director_id == Movie.director_id)
        if genre_id:
            query = query.filter(genre_id == Movie.genre_id)
        if year:
            query = query.filter(year == Movie.year)
        return MovieSchema(many=True).dump(query.all()), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return '', 201


@movie_ns.route('/<int:mid>')
class MoviesViews(Resource):
    def get(self, mid: int):  # получение данных
        try:
            movie = movie_service.get_one(mid)
            return movies_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, mid: int):  # замена данных
        req_json = request.json
        req_json["id"] = mid

        movie_service.update(req_json)

        return '', 204

    def patch(self, mid: int):  # частичное обновление данных
        req_json = request.json
        req_json["id"] = mid

        movie_service.update_partial(req_json)

        return '', 204

    def delete(self, mid: int):
        movie_service.delete(mid)

        return '', 204
