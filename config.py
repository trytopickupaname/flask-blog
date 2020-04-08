# import sys
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# BASE_URI = 'mysql+pymysql://root:lpj12345@localhost:3306/flaskblog?charset=utf8'
# BASE_URI = 'mysql+pymysql://ll_admin:lpj12345@localhost:3306/flaskblog?charset=utf8'


class Config(object):
    # SECRET_KEY = 'ZaW3IOWIC7V#0TgKYg32T8w'
    # SQLALCHEMY_DATABASE_URI = BASE_URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
