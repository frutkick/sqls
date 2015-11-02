from flask import Flask, render_template, request

from ecomap.db import util

app = Flask(__name__, template_folder='.')


@app.route('/')
def func():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return request.json['email']


@app.route('/register', methods=['GET', 'POST'])
def register():
    json = request.json
    util.create_user(json)
    return request.json

if __name__ == '__main__':
    app.run()
