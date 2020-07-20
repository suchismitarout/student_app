from flask import Flask
import os
from app.database import db
from app.api.student_api import student_route
from app.api.department_api import dept_route
from app.api.homepage_api import home_route
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    app.config['SECRET_KEY'] = 'myseckey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(student_route)
    logging.debug("in student_api")
    app.register_blueprint(dept_route)
    logging.debug("in dept_api")
    app.register_blueprint(home_route)
    return app


