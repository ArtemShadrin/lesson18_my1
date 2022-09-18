from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.models.director import DirectorSchema

director_ns = Namespace('directors')
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema


@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)

        return '', 201


@director_ns.route('/<int:did>')
class DirectorsViews(Resource):
    def get(self, did: int):  # получение данных
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, did: int):  # замена данных
        req_json = request.json
        req_json["id"] = did

        director_service.update(req_json)

        return '', 204

    def patch(self, did: int):  # частичное обновление данных
        req_json = request.json
        req_json["id"] = did

        director_service.update_partial(req_json)

        return '', 204

    def delete(self, did: int):
        director_service.delete(did)

        return '', 204
