from flask import Flask

app = Flask(__name__)
#配置文件
app.config.from_object("settings.DevelopmentConfig")


@app.route('/index', methods=['GET', 'POST'])
def index():
    return ""


if __name__ == '__main__':
    app.run()
