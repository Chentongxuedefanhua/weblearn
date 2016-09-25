#coding: utf-8

"""
@file: forms.py
@time: 2016/9/20 
@author: chenfan
"""
from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Regexp,EqualTo,Email

class LoginFrom(Form):
    username=StringField(label=u'账号',validators=[DataRequired()])
    password=PasswordField(label=u'密码',validators=[DataRequired()])
    submit=SubmitField(label=u'提交')

class RegistrationFrom(Form):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64), Email(u'邮箱格式错误')])
    username = StringField(u'用户名',validators=[DataRequired(),
                                              Length(1,64),
                                              Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                     u'用户名必须有字母、数字、下划线或.组成')])
    password = PasswordField(u'密码',validators=[DataRequired()])
    password2 = PasswordField(u'确认密码',validators=[DataRequired(),
                                                 EqualTo('password',u'密码必须一致')])

    submit = SubmitField(u'注册')
