from flask import Flask,session
from flask_session import RedisSessionInterface


app = Flask(__name__)
app.secret_key='hhalhda'

#方式一 redis保存session
# from redis import Redis
# app.session_interface = RedisSessionInterface(
#     redis=Redis(host='127.0.0.1', port=6379),
#     key_prefix='flaskXXX'
# )

#方式二 ：redis保存session
# from flask.ext.session import Session
from flask_session import Session
from redis import Redis
app.config['SESSION_TYPE']='redis'
app.configp['SESSION_REDIS']=Redis(host='192.168.1.1',port='6379')
Session(app)



@app.route('/login')
def login():
    session['key']=123
    return 'login'


@app.route('/index')
def index():
    val=session['key']
    print(val)
    return 'Index'


if __name__ == '__main__':
    app.run()
