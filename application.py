import os

from flask import Flask, render_template, request
from flask_restful import Api
import requests

from rest_store.store import LocalStore
from forms import TestForm, SearchForm

application = Flask(__name__)

application.config['WTF_CSRF_SECRET_KEY'] = os.urandom(24)
application.config['SECRET_KEY'] = os.urandom(24)

api = Api(application)
api.add_resource(LocalStore, "/store/<local>/<query>/<page>")


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


@application.route('/page', methods=['GET', 'POST'])
def page():
    form = SearchForm()
    page = 0
    result = {
        'result': 'None'
    }
    if request.method == "GET":
        return render_template('page.html', form=form, nav_menu='page', page=page, result=result)

    if request.method == 'POST':
        if form.validate_on_submit():
            loc = request.form.get('location')
            query = request.form.get('query')

            #왼쪽 버튼 오른쪽 버튼, 검색 버튼에 따른 page수 조정
            page = request.form.get('page')
            if page is None or int(page) == 0:
                page = 1
            else :
                page = int(page)
                if "next" in request.form:
                    page += 1
                elif "prev" in request.form:
                    page -= 1
                elif "search" in request.form:
                    page = 1
            url = 'http://localhost:8080/store/{0}/{1}/{2}'.format(loc, query, page)
            result = requests.get(url).json()
        return render_template('page.html', form=form, nav_menu='page', page=page, result=result)


if __name__ == '__main__':
    host_addr = '0.0.0.0'
    port_num = '8080'
    application.run(host=host_addr, port=port_num, debug=True, threaded=True)