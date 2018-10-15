from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/test1')
def test1():
    print('this is test1')
    return redirect(url_for('test2'))


@app.route('/test2')
def test2():
    print('this is test2')
    return 'this is test2'


if __name__ == '__main__':
    app.run(port=5000, debug=True)