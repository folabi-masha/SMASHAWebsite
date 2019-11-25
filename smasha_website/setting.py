import os

import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
