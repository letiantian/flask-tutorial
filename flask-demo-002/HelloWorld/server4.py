from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    r = request.args.get('info')
    if r==None:
        # do something
        return ''
    return r

if __name__ == '__main__':
    app.run(port=5000, debug=True)