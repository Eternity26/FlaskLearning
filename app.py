from flask import Flask

import settings

app = Flask(__name__)

app.config.from_object(settings)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/lol')
def lol():
    return '<font color="blue">lol</font>'


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
