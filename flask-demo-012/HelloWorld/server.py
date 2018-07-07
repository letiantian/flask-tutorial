from flask import Flask, request, Response, make_response
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/add')
def login():
    res = Response('add cookies')
    res.set_cookie(key='name', value='letian', expires=time.time()+6*60)
    return res


@app.route('/show')
def show():
    return request.cookies.__str__()


@app.route('/del')
def del_cookie():
    res = Response('delete cookies')
    res.set_cookie('name', '', expires=0)
    return res


if __name__ == '__main__':
    app.run(port=5000, debug=True)