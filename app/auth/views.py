#coding: utf-8

"""
@file: views.py
@time: 2016/9/25
@author: chenfan
"""
from flask import render_template,flash,redirect,url_for
from . import auth
from forms import LoginFrom,RegistrationFrom
from ..models  import db,User,Role

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginFrom()
    flash(u'登录成功!')
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
    return render_template('registra.html', form=form)

@auth.route('/loginout')
def loginout():
    pass
