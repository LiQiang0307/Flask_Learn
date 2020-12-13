from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = "kkl"


# 检查是否已经登录
@app.before_request
def checklogin():
    if request.path == '/login':
        return None
    user = session.get('user_info')
    if not user:
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return "LOGIN"


@app.route('/index', methods=['GET', 'POST'])
def login():
    return "INDEX"


if __name__ == '__main__':
    app.run()
