from flask import Flask

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'], defaults={'db': 'xxxx'})
def index(db):
    return "Index"


"""
 strict_slashes=False 时 
 http://127.0.0.1:5000/login/ 可以访问
 http://127.0.0.1:5000/login 可以访问
"""


@app.route('/login', strict_slashes=False)
def login():
    return "Login"


"""
strict_slashes=True时
http://127.0.0.1:5000/loginout 可以访问
http://127.0.0.1:5000/loginout/ 不可以访问
"""


@app.route('/loginout', strict_slashes=True)
def loginout():
    return "Loginout"


@app.route('/hello',redirect_to='/world') # redirect_to 重定向url  访问http://127.0.0.1:5000/hello 跳转到 http://127.0.0.1:5000/world （js也可以做重定向）
def hello():
    return "hello"


@app.route('/world')
def world():
    return "world"


if __name__ == '__main__':
    app.run()
