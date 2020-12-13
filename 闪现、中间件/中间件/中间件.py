from flask import Flask

app = Flask(__name__)
app.secret_key = "1111111"


@app.route('/x2', methods=['GET', 'POST'])
def index():
    return "x2"


class Middleware(object):
    def __init__(self, old_wsgi_app):
        """
        服务端启动时，自动执行
        :param old_wsgi_app:
        """
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        """
        每次用户请求到来时
        :param args:
        :param kwargs:
        :return:
        """
        print('before')
        obj = self.old_wsgi_app(environ, start_response)
        print('after')
        return obj


if __name__ == '__main__':
    app.wsgi_app = Middleware(app.wsgi_app)
    app.run()
    """
    1.执行app.__call__
    2.调用app.wsgi_app方法
    """
