#coding:utf-8

from flask import render_template,request
from app import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return 'about'

@main.route('/service')
def service():
    return 'service'

@main.route('/project')
def project():
    return 'project'

@main.route('/tables')
def tables():
    data = [{
            "name": "bootstrap-table",
            "commits": "10",
            "attention": "122",
            "uneven": "An extended Bootstrap table"
        }]
    return render_template('table.html', data=data )

