#coding: utf-8
from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Interval, primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    users = db.relationship('User', backref='roles')

    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(r),['Guests','Admin']))
        db.session.commit()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Interval, primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    role_id = db.Column(db.Interval,db.ForeignKey('roles.id'))

    @staticmethod
    def on_create(tagert, value, initiator):
        tagert.role = Role.query.filter_by(name='Guests').first



