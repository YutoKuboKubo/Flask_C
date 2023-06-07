from myapp import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime


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

    # パスワードが正しいか確認
    def validate_password(self, password):
        return check_password_hash(self.password, password)

    # dbにユーザを追加
    def create_new_user(self):
        db.session.add(self)

    # idに該当するユーザを取得
    @classmethod
    def select_user_by_id(cls, id):
        return cls.query.get(id)

    # usernameに該当するユーザを取得
    @classmethod
    def select_user_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


class Tweets(db.Model):

    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    picture_path = db.Column(db.Text)
    body = db.Column(db.Text)
    from_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    from_user_name = db.Column(db.String(10))
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title, body, picture_path, from_user_id, from_user_name):
        self.title = title
        self.body = body
        self.picture_path = picture_path
        self.from_user_id = from_user_id
        self.from_user_name = from_user_name


    def create_tweet(self):
        db.session.add(self)
