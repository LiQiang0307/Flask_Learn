import functools

from flask import Flask

app = Flask(__name__)


def wapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        print('before')
        return func(*args,**kwargs)
    return inner


@app.route('/index', methods=['GET', 'POST'])
@wapper#装饰器写在下面
def index():
    return "INDEX"


@app.route('/xxx', methods=['GET', 'POST'])
@wapper
def xxx():
    return "xxx"


if __name__ == '__main__':
    app.run()
