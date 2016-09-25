#coding:utf-8

from flask import render_template,request,flash
from forms import LoginFrom
def init_views(app):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return 'about'

    @app.route('/service')
    def service():
        return 'service'

    @app.route('/project')
    def project():
        return 'project'

    @app.route('/login')
    def login():
        form = LoginFrom()
        flash(u'登录成功！')
        return render_template('login.html',tilte=u'登录',form=form)

    @app.template_test('current_link')
    def is_current_link(link):
        return link == request.path