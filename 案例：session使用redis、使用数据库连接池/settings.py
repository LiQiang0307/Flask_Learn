from datetime import timedelta
from redis import Redis


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = "123"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)  # 20分钟后session失效
    SESSION_REFERSH_EACH_REQUEST = True
    #使用redis  如果使用本地，将下面两行注释
    SESSION_TYPE='redis'
    SESSION_REDIS=Redis(host='127.0.0.1',port='6379')
    PYMYSQL_HOST='127.0.0.1'

class ProductionConfig(BaseConfig):
    # DEBUG = False
    pass


class DevelopmentConfig(BaseConfig):
    # DATABASE_URL = 'mysql://user@dev/foo'
    pass


class TestingConfig(BaseConfig):
    pass
    # DATABASE_URL = 'mysql://user@test/foo'
