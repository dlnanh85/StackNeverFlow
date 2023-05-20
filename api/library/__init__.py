from flask import Flask
from .api import api
from .extension import db
from .extension import ma
from .model import User, Blog, Tag, Tag_Blog


def create_db(app):
    with app.app_context():
        db.create_all()
        print('Database created!')


def create_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    app.register_blueprint(api)
    return app