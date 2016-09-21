#coding:utf-8

from app import db


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
