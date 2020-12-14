from flask import Flask
from flask_session import Session
from .views import home
from .views import account
from pro_flask.utils.pool import init_pool


def create_app():
    app=Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')

    app.register_blueprint(account.account)
    app.register_blueprint(home.home)

    #将session替换成redis
    Session(app)
    init_pool(app)

    return app