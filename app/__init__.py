#!/usr/bin/env python
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
from forms import LoginFrom
from flask_sqlalchemy import SQLAlchemy
#导入视图
from app.views import init_views

bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    # 读取配置文件
    app.config.from_pyfile('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/web'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # 生成一个导航栏
    nav.register_element('top', Navbar(u'Flask入门',
                                   View(u'主页', 'index'),
                                   View(u'关于', 'about'),
                                   View(u'服务', 'service'),
                                   View(u'项目', 'project'),
                                   ))
    #注册bootstrap
    bootstrap.init_app(app)
    nav.init_app(app)
    db.init_app(app)
    init_views(app)
    return app










