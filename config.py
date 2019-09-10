class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/api_crud_db'


class Development(BaseConfig):
    DEBUG = True


class Production(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ''

class Testing(BaseConfigs):
    TESTING = True
