from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/page/<int:num1>-<int:num2>')
def page(num1, num2):
    print(num1)
    print(num2)
    return 'hello world'


if __name__ == '__main__':
    app.run(port=5000, debug=True)