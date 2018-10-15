from flask import Flask, request, Response
import json

app = Flask("my-app")


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add', methods=['POST'])
def add():
    result = {'sum': request.json['a'] + request.json['b']}
    return Response(json.dumps(result),  mimetype='application/json')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)