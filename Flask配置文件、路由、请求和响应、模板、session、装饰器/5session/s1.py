"""
session 流程：
1.请求刚刚到达
    ctx=RequestContext（）
        -request
        -session=None
    ctx.push()
        ctx.session=SecureCookieSessionInterface.open_session

2.视图函数

3.请求结束
    SecureCookieSessionInterface.save_session()

"""

from flask import Flask, session

app = Flask(__name__)
app.secret_key = "yuio"


@app.route('/x1')
def index():
    session['k1'] = 123
    session['k2'] = 123
    del session['k2']
    return "Index"


@app.route('/x2')
def order():
    print(session['k1'])
    return "Order"


if __name__ == '__main__':
    app.run()
