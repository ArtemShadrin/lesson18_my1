# main.py
from flask_restx import Api

from app.config import Config
from app.database import db
from flask import Flask


from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.directors import director_ns

def create_app(config: Config) -> Flask:
    """
    Создаем приложение и возвращаем его
    """
    application = Flask(__name__)
    application.config.from_object(config)   # грузим конфигурацию из объекта
    application.app_context().push()  # применяем конфигурацию во всех его будущих компонентах
    return application

def configure_app(application: Flask):
    """
    Конфигурация приложения
    """
    db.init_app(application)
    api = Api(app)
    # подключаем namespace
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':  # если приложение запущенно то
    app_config = Config()  # создаем конфигурацию
    app = create_app(app_config)  # запускаем конфигурацию
    configure_app(app)  # добавляем функцию
    app.run()
