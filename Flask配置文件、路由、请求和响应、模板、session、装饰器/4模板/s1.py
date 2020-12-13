from flask import Flask, render_template, Markup

app = Flask(__name__)


# 全局，每个模板里都可以使用这个函数
@app.template_global()
def sb(a1, a2):
    return a1 + a2


def gen_input(value):
    # return "<input value='%s'/>" %value
    return Markup("<input value='%s'/>" % value)


@app.route('/index', methods=['GET', 'POST'])
def index():
    context = {
        'k1': 123,
        'k2': [11, 22, 33],
        'k3': {'name': 'liq', 'age': '12'},
        'k4': lambda x: x + 1,
        'k5': gen_input  # 只有当前模板才能调用的函数
    }
    return render_template('index.html', **context)


@app.route('/order', methods=['GET', 'POST'])
def order():
    context = {
        'k1': 123,
        'k2': [11, 22, 33],
    }
    return render_template('order.html', **context)


if __name__ == '__main__':
    app.run()
