from flask import Blueprint

us = Blueprint('us', __name__)


@us.route('/info')
def info():
    return "info"
