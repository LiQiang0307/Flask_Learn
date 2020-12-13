from flask import Blueprint,render_template

ac = Blueprint('ac', __name__)


@ac.route('/login')
def login():
    # return "login"
    return render_template('login.html')


@ac.route('/logout')
def logout():
    return "logout"
