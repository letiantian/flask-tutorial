from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.args)
    r = request.args.get('p')
    return r


if __name__ == '__main__':
    app.run(port=5000, debug=True)