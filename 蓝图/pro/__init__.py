from flask import Flask

app = Flask(__name__)

from .views import account
from .views import admin
from .views import user

app.register_blueprint(account.ac)
app.register_blueprint(admin.ad)
app.register_blueprint(user.us)

"""
蓝图目录结构的划分，url的划分
"""