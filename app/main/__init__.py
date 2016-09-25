#coding: utf-8

"""
@file: __init__.py.py
@time: 2016/9/25 
@author: chenfan
"""
from flask import Blueprint


main = Blueprint('main', __name__)

import views