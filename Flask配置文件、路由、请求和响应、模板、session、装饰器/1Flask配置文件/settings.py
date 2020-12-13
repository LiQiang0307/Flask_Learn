class BaseConfig(object):
    DEBUG=True
    TESTING=False
    DATABASE_URL='sqlite://:memory:'
    SECRET_KEY="123"


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    # DATABASE_URL = 'mysql://user@dev/foo'
    pass


class TestingConfig(BaseConfig):
    pass
    # DATABASE_URL = 'mysql://user@test/foo'