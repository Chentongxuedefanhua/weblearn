#!/usr/bin/env python
#coding: utf-8

"""
@file: index.py
@time: 2016/9/20 
@author: chenfan
"""
from flask import Flask,url_for,render_template,request,flash
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from forms import LoginFrom
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#读取配置文件
app.config.from_pyfile('config')
#注册bootstrap
Bootstrap(app)

nav = Nav()
#生成一个导航栏
nav.register_element('top', Navbar(u'Flask入门',
                                   View(u'主页','index'),
                                   View(u'关于','about'),
                                   View(u'服务','service'),
                                   View(u'项目','project'),
))
nav.init_app(app)
#导航栏完成

#数据库
app.config.from_pyfile('config')['SQLALCHEMY_DATABASE_URL'] = True
db = SQLAlchemy(app)
class Role(db.Model):
    tablename = 'role'
    id = db.Column(db.Interval, primary_key=True)
    name = db.Column(db.String, nullable=True)

class User(db.Model):
    tablename = 'users'
    id = db.Column(db.Interval, primary_key=True)
    name = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)
#数据库结束


@app.template_test('current_link')
def is_current_link(link):
    return link == request.path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'about'

@app.route('/service')
def service():
    return 'service'

@app.route('/project')
def project():
    return 'project'

@app.route('/login')
def login():
    form = LoginFrom()
    flash(u'登录成功！')
    return render_template('login.html',tilte=u'登录',form=form)

if __name__ == '__main__':
    app.run()