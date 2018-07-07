from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return request.args.get('info')


if __name__ == '__main__':
    app.run(port=5000, debug=True)