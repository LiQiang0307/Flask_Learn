from flask import Blueprint

ad = Blueprint('ad', __name__, url_prefix='/admin')  # 某一类url加前缀  static_folder


@ad.before_request
def bf():
    print("before_request")


@ad.route('/home')
def home():
    return "home"


@ad.route('/index')
def index():
    return "index"
