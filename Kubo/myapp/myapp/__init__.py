import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('myapp.config')

db = SQLAlchemy(app)

from myapp.views import log, tweet, user

login_manager = LoginManager()
login_manager.init_app(app)

# ログインのコールバック用
from myapp.models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
