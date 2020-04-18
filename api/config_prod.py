import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f3e687f82be0ecd2f9d83352b7f0b8ff96d954a68cfee5c9'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WORDSAPI_KEY = os.environ.get('WORDSAPI_KEY')
    WORDSAPI_HOST = os.environ.get('WORDSAPI_HOST')

