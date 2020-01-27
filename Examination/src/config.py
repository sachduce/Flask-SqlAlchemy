import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '\x9b\xc3bY\xed\xa6=m\xb4\xdc\xee\x8f>\xdd6\xb5~\xcf\x8f=\x03\xea2\xa4'
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'examination.db')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "localhost"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'examination.db')


config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestingConfig,
    prod = ProductionConfig
)