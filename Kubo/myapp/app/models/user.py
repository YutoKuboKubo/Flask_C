from app import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# ユーザのモデル
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

    # usernameに該当するユーザを取得
    @classmethod
    def select_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def validate_password(self, password):
        return check_password_hash(self.password, password)

