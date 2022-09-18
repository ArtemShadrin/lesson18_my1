from marshmallow import Schema, fields

from app.database import db
from app.dao.models.director import DirectorSchema
from app.dao.models.genre import GenreSchema


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    # .Pluck ('указываем схему', 'указываем строку которую хотим вывести')
    genre = fields.Nested(GenreSchema)
    # .Nested позволяет связать данные с др. схемами (по умолчанию все но через ['имя колонки']
    director = fields.Nested(DirectorSchema)
