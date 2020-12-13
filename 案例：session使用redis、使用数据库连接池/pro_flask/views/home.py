from flask import Blueprint, session

home = Blueprint('home', __name__)


@home.route('/index')
def index():
    user_info = session.get('user_info')
    print('原来的值',user_info)
    session['user_info']['k1']=9999999
    user_info = session.get('user_info')
    print('修改后的值',user_info)
    # session['modified']=True
    return "INDEX"


@home.route('/test')
def test():
    user_info = session.get('user_info')
    print(user_info)
    return "test"
