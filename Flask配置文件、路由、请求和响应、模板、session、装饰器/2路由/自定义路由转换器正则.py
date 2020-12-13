from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 自定义路由转换器
@app.route('/index/<int:nid>', methods=['GET', 'POST'])  # http://127.0.0.1:5000/index/2
def index(nid):
    print(nid)
    return "Index"


class RegexConvertetr(BaseConverter):
    """
    自定义正则表达式
    """

    def __init__(self, map, regex):
        super(RegexConvertetr, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value:
        :return:
        """
        return int(value)

    def to_url(self, value):
        """
        使用url_for 反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        """
        val = super(RegexConvertetr, self).to_url(value)
        return val


app.url_map.converters['regex'] = RegexConvertetr


@app.route('/login/<regex("\d+"):nid>', methods=['GET', 'POST'])  # http://127.0.0.1:5000/login/234
def login(nid):
    print(nid)
    v = url_for('index', nid=999)  # /index/999
    print(v)
    return "Login"


if __name__ == '__main__':
    app.run()
