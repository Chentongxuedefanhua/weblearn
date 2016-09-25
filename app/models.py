#coding: utf-8
from app import db
from app import create_app
db.app = create_app()
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Interval, primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    users = db.relationship('User', backref='roles')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Interval, primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    role_id = db.Column(db.Interval,db.ForeignKey('roles.id'))

db.create_all()
