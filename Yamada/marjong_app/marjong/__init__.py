from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('marjong.config')

db = SQLAlchemy(app)

from marjong.views import views