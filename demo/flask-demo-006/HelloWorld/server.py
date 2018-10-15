from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/user/<username>')
def user(username):
    print(username)
    print(type(username))
    return 'hello ' + username


@app.route('/user/<username>/friends')
def user_friends(username):
    print(username)
    print(type(username))
    return 'Hello {}. They are your friends.'.format(username)


if __name__ == '__main__':
    app.run(port=5000, debug=True)