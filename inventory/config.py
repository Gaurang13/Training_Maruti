import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(32)

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True

class Db_Config(Config):
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = 'Mtech@12345'
    DB = 'inventory'
    CHARSET = 'utf8mb4'
    CURSORCLASS = 'pymysql.cursors.DictCursor'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = 'any'
