from uuid import uuid4
from ..utils.sql import SQLHelper
from flask import Blueprint, render_template, request, session, redirect,current_app

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    print(current_app.config['PYMYSQL_HOST'])
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    obj=SQLHelper.fetch_one("select id,name from user_tb where name =%s and password=%s",[user,pwd])

    if obj:
    # if user == 'alex' and pwd == '123':
        session.permanent=True
        session['user_info'] = {'id': obj['id'], 'name': user}
        return redirect('/index')
    else:
        return render_template('login.html',msg="用户名或密码错误")

