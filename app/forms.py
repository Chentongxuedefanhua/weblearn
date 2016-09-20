#!/usr/bin/env python
#coding: utf-8

"""
@file: forms.py
@time: 2016/9/20 
@author: chenfan
"""
from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginFrom(Form):
    username=StringField(label=u'账号',validators=[DataRequired()])
    password=PasswordField(label=u'密码',validators=[DataRequired()])
    submit=SubmitField(label=u'提交')

