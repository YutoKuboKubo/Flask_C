from app import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(128), default=generate_password_hash('myapp'))
    picture_path = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<Entry id:{} username:{} password:{}>'.format(self.id, self.username, self.password)
