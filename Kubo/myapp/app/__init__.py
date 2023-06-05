import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__name__))
app = Flask(__name__)
app.config.from_object('app.config')

db = SQLAlchemy(app)

from app.views import log
login_manager = LoginManager()
login_manager.login_view = 'app.view'
login_manager.login_message = 'ログインしてください'
login_manager.init_app(app)