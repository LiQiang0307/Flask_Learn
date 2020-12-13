from flask import Flask

app = Flask(__name__)

"""
before_request=[xxx,xxx_]
"""


@app.before_request
def xxx():
    print("前1")


@app.before_request
def xxx_():
    print("前2")


"""
after_request=[xxxx,xxxx_]
reversed()
[xxxx_,xxxx]翻转
"""


@app.after_request
def xxxx(response):
    # print(response)
    print("后1")
    return response


@app.after_request
def xxxx_(response):
    # print(response)
    print("后2")
    return response


@app.route('/x1', methods=['GET', 'POST'])
def x1():
    print("视图函数x1")
    return "视图函数x1 "


@app.route('/x2', methods=['GET', 'POST'])
def x2():
    print("视图函数x2")
    return "视图函数x2"


if __name__ == '__main__':
    app.run()
