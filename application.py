import os

from flask import Flask, render_template, request
from flask_restful import Api
from flaskext.markdown import Markdown
import requests

from rest_store.store import LocalStore
from forms import TestForm

application = Flask(__name__)

application.config['WTF_CSRF_SECRET_KEY'] = os.urandom(24)
application.config['SECRET_KEY'] = os.urandom(24)

Markdown(application)

api = Api(application)
api.add_resource(LocalStore, "/store/<local>/<query>/<page>")


@application.errorhandler(404)
def page_not_found(error):
    print("parameter error")
    return {'result':404}, 404


@application.route('/', methods=['GET', 'POST'])
def home():
    form = TestForm(url='http://localhost:8080/store/평택시/폐계닭/1')
    result = {
        'result': 'None'
    }

    if request.method == 'GET':
        return render_template('request.html', nav_menu='request', form=form, result=result)

    if request.method == 'POST':
        if form.validate_on_submit():
            result = requests.get(request.form['url']).json()
            return render_template('request.html', nav_menu='request', form=form, result=result)


@application.route('/readme')
def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template('readme.html', nav_menu='readme', readme=content)


@application.route('/page')
def page():
    return render_template('page.html', nav_menu='page')


if __name__ == '__main__':
    host_addr = '0.0.0.0'
    port_num = '8080'
    application.run(host=host_addr, port=port_num, debug=True, threaded=True)