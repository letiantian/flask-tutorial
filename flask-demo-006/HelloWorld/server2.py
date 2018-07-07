from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/page/<int:num>')
def page(num):
    print(num)
    print(type(num))
    return 'hello world'


if __name__ == '__main__':
    app.run(port=5000, debug=True)