from flask import Flask, render_template, request

from ecomap.db import util
import logging

app = Flask(__name__, template_folder='.')


@app.route('/')
def func():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    result = util.login(request.json)
    logging.getLogger('view').info('Got responce from db: %s', result)
    return result['first_name']


@app.route('/register', methods=['GET', 'POST'])
def register():
    util.create_user(request.json)
    return request.json['first_name']

if __name__ == '__main__':
    app.run()
