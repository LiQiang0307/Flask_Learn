from flask import Flask

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'], subdomain="<username>")#获取子域名
def index(username):
    print(username)
    return "Index"


if __name__ == '__main__':
    app.run()
