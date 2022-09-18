from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.models.genre import GenreSchema

genre_ns = Namespace('genres')
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        genre_service.create(req_json)

        return '', 201


@genre_ns.route('/<int:gid>')
class GenresViews(Resource):
    def get(self, gid: int):  # получение данных
        try:
            genre = genre_service.get_one(gid)
            return genres_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404

    def put(self, gid: int):  # замена данных
        req_json = request.json
        req_json["id"] = gid

        genre_service.update(req_json)

        return '', 204

    def patch(self, gid: int):  # частичное обновление данных
        req_json = request.json
        req_json["id"] = gid

        genre_service.update_partial(req_json)

        return '', 204

    def delete(self, gid: int):
        genre_service.delete(gid)

        return '', 204
