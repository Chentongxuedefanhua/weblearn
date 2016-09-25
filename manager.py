#!/usr/bin/env python
#coding: utf-8

"""
@file: manager.py
@time: 2016/9/24 
@author: chenfan
"""
from flask_script import Manager
#from app import create_app
from test import create_app
app = create_app()
manager = Manager(app)

@manager.command
def dev():
    from livereload import Server
    live = Server(app.wsgi_app)
    live.watch('**/*.*')
    live.serve(open_url=True)

@manager.command
def test():
    pass

if __name__ == '__main__':
    manager.run()