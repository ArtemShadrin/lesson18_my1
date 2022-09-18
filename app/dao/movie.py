from app.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def get_all(self):
        pass

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie


    def delete(self, mid):
        movie = self.session.query(Movie).get(mid)

        self.session.delete(movie)
        self.session.commit()