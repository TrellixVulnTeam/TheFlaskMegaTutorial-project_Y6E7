import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's3cur1t3y'