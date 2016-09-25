#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    db.init_app(app)
    db.app = app

    return app