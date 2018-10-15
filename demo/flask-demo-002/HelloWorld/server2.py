from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.path)
    print(request.full_path)
    return request.args.__str__()


if __name__ == '__main__':
    app.run(port=5000, debug=True)