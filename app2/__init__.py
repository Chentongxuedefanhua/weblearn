#coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def creat_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db.init_app(app)
    return app
