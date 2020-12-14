from uuid import uuid4
from ..utils.sql import SQLHelper
from flask import Blueprint, render_template, request, session, redirect,current_app

account = Blueprint('account', __name__)


from wtforms import Form
from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets


class LoginForm(Form):
    user = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            # validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(), #页面上生成input 标签
        render_kw={'class': 'form-control'}  #显示属性
    )
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            # validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            # validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
            #                   message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form=LoginForm()
        return render_template('login.html',form=form)
    # user = request.form.get('user')
    # pwd = request.form.get('pwd')
    form =LoginForm(formdata=request.form)
    if not form.validate():
        print('用户提交数据通过格式验证，提交的值为：',form.data)
        return render_template('login.html',form=form)

    obj=SQLHelper.fetch_one("select id,name from user_tb where name =%(user)s and password=%(pwd)s",form.data)
    if obj:
    # if user == 'alex' and pwd == '123':
        session.permanent=True
        session['user_info'] = {'id': obj['id'], 'name': obj['name']}
        return redirect('/index')
    else:
        return render_template('login.html',msg="用户名或密码错误",form=form)


# ########################### 用户注册 ##########################
class RegisterForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='alex'
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(
            (1, '男'),
            (2, '女'),
        ),
        coerce=int
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
        # choices=SQLHelper.fetch_all('select id,name from city',{})
    )

    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))

    def validate_pwd_confirm(self, field):
        """
        自定义pwd_confirm字段规则，例：与pwd字段是否一致
        :param field:
        :return:
        """
        # 最开始初始化时，self.data中已经有所有的值

        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证




@account.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        form=RegisterForm()
        return render_template('register.html',form=form)
    form=RegisterForm(formdata=request.form)
    if form.validate():
        print(form.data)
    else:
        print(form.errors)
    return 'qqqq'