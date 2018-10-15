from flask import Flask, render_template_string, abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/user')
def user():
    abort(401)  # Unauthorized 未授权
    print('Unauthorized, 请先登录')


if __name__ == '__main__':
    app.run(port=5000, debug=True)