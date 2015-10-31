from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')


@app.route('/')
def func():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return request.json['email']


@app.route('/register', methods=['GET', 'POST'])
def register():
    return request.json

if __name__ == '__main__':
    app.run()
