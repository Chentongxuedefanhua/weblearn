#!/usr/bin/env python
#coding: utf-8

"""
@file: manager.py
@time: 2016/9/24 
@author: chenfan
"""
from flask_script import Manager
from app import create_app
from app.model_base import db
from flask_migrate import Migrate, MigrateCommand,upgrade
from app.models import Role,User

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
@manager.command
def dev():
    from livereload import Server
    live = Server(app.wsgi_app)
    live.watch('**/*.*')
    live.serve(open_url=True)

@manager.command
def test():
    pass



@manager.command
def deploy():
    upgrade()
    Role.seed()


if __name__ == '__main__':
    manager.run()