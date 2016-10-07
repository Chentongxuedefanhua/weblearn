#coding: utf-8

"""
@file: views.py
@time: 2016/9/25
@author: chenfan
"""
from flask import render_template,flash,redirect,url_for
from app.auth import auth
from forms import LoginFrom,RegistrationFrom
from app.models import User
from app.model_base import db
from flask_login import login_user,logout_user

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data, password=form.password.data).first()
        if user is not None:
            login_user(user)
            flash(u'登录成功!')
            return redirect(url_for('main.index'))
    return render_template('login.html', tilte=u'登录', form=form)

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    name=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('registra.html', form=form,title=u'注册')

@auth.route('/loginout')
def loginout():
    logout_user()
    return redirect(url_for('auth.login'))
