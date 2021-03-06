import os


class BaseConfig:
    pass


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_ECHO = True


class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True


class ProdConfig(BaseConfig):
    pass


configurations = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}
