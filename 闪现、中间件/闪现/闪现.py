from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = "1111111"


@app.route('/x1', methods=['GET', 'POST'])
def login():
    # session['msg'] = 'abcd'
    flash("我是xxxx1", category='x1')
    flash("我是xxxx2", category='x2')
    return ""


@app.route('/x2', methods=['GET', 'POST'])
def index():
    # msg = session.pop('msg') #可以用session实现闪现
    # msg=get_flashed_messages()
    msg = get_flashed_messages(category_filter=['x1'])  # 可以指定类别
    print(msg)
    return ""


if __name__ == '__main__':
    app.run()
