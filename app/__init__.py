#coding: utf-8

"""
@file: __init__.py
@time: 2016/9/20 
@author: chenfan
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from model_base import db
from app.auth.forms import LoginFrom


bootstrap = Bootstrap()
nav = Nav()

def create_app():
    app = Flask(__name__)
    # 读取配置文件
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/web'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db.init_app(app)
    # 生成一个导航栏
    nav.register_element('top', Navbar(u'Flask入门',
                                   View(u'主页', 'main.index'),
                                   View(u'关于', 'main.about'),
                                   View(u'服务', 'main.service'),
                                   View(u'项目', 'main.project'),
                                   ))
    #注册bootstrap
    bootstrap.init_app(app)
    nav.init_app(app)

    from auth import auth as auth_blueprint
    from main import main as mainn_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(mainn_blueprint)

    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path
    return app










