import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's3cur1t3y'
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ...
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or "localhost"
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ... mail_to
    MAIL_ADMIN = os.environ.get('MAIL_ADMIN') or ['admin@example.com']
    # ... Pagination
    POSTS_PER_PAGE=3

    #Babel
    LANGUAGES=['en','ru']

    #MS Azure Translation API
    MS_TRANSLATOR_APIKEY = os.environ.get('MS_TRANSLATOR_APIKEY')
    MS_TRANSLATOR_API = os.environ.get('MS_TRANSLATOR_API')