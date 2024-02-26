import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(object):
    SECRET_KEY = 'secretkey - change for production'
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_RELOADER = True

class ProductionConfig(object):
    SECRET_KEY = 'secretkey - change for production'
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.db')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False