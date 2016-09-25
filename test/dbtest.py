#!/usr/bin/env python
#coding:utf-8

'''
@auth:chenfan
@time:2016/9/21
'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/web'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy()
db.init_app(app)
db.app = app
class Metrics(db.Model):
    __tablename__ = 'monitor_metric'
    id = db.Column(db.Integer,primary_key=True)
    layered = db.Column(db.String(64),default='', nullable=False, doc=u'层级')
    application = db.Column(db.String(64),default='', nullable=False, doc=u'应用')
    monitor_metric = db.Column(db.String(64),default='', nullable=False, doc=u'监控指标')
    description = db.Column(db.String(64),default='', nullable=False, doc=u'指标描述')
    key = db.Column(db.String(64),default='', nullable=False, doc=u'对应的key值')
    trigger = db.Column(db.String(64),default='', nullable=False, doc=u'告警设置')
    influence = db.Column(db.String(64),default='', nullable=False, doc=u'告警影响')
    reason = db.Column(db.String(64),default='', nullable=False, doc=u'原因')
if __name__ == '__main__':
    db.create_all()