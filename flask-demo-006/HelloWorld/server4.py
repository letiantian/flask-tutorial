from flask import Flask, url_for

from werkzeug.routing import BaseConverter


class MyIntConverter(BaseConverter):

    def __init__(self, url_map):
        super(MyIntConverter, self).__init__(url_map)

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value * 2


app = Flask(__name__)
app.url_map.converters['my_int'] = MyIntConverter


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/page/<my_int:num>')
def page(num):
    print(num)
    print(url_for('page', num=123))   # page 对应的是 page函数 ，num 对应对应`/page/<my_int:num>`中的num，必须是str
    return 'hello world'


if __name__ == '__main__':
    app.run(port=5000, debug=True)