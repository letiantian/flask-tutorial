from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    pass


@app.route('/user/<name>')
def user(name):
    pass


@app.route('/page/<int:num>')
def page(num):
    pass


@app.route('/test')
def test():
    print(url_for('hello_world'))
    print(url_for('user', name='letian'))
    print(url_for('page', num=1, q='hadoop mapreduce 10%3'))
    print(url_for('static', filename='uploads/01.jpg'))
    return 'Hello'


if __name__ == '__main__':
    app.run(port=5000, debug=True)