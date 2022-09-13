from marshmallow import Schema, fields


class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()


class MovieSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Float()
    # .Pluck ('указываем схему', 'указываем строку которую хотим вывести')
    genre = fields.Pluck(GenreSchema, 'name')
    # .Nested позволяет связать данные с др. схемами (по умолчанию все но через ['имя колонки']
    director = fields.Nested(DirectorSchema)
