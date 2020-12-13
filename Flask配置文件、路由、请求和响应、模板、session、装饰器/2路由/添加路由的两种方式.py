from flask import Flask

app = Flask(__name__)

"""
1.执行decorator=app.route('/index', methods=['GET', 'POST'])
2.@decorator 
    -新index=decorator（index）
"""


# 添加路由方式一（一般情况下都是使用此方式）
@app.route('/index', methods=['GET', 'POST'])
def index():
    return ""


# 添加路由方式二
def order():
    return 'Order'


app.add_url_rule('/order', view_func=order)

if __name__ == '__main__':
    app.run()
