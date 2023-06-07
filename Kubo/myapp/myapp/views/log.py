from flask import (
    request, redirect, url_for, render_template,
    flash, session
)
from myapp import app, db
from myapp.models.user import User
from flask_login import (
    login_user, login_required, logout_user, current_user
)
from flask_bcrypt import generate_password_hash


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    '''新規登録メソッド'''
    if request.method == "POST":
        user = User(
            username=request.form['username'],
            password=generate_password_hash(request.form['password']) # パスワードをハッシュ化
        )
        # データベースに追加
        user.create_new_user()
        db.session.commit()
        flash('新規登録が完了しました')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''ログイン用'''
    if request.method == "POST":
        # ログインしようとしているユーザを取得
        user = User.select_user_by_username(request.form['username'])
        # ユーザが存在し、かつパスワードが会っていた場合
        if user and user.validate_password(request.form['password']):
            # ログイン
            login_user(user, remember=True)
            return redirect(url_for('home'))
        elif not user:
            flash('存在しないユーザです')
            return redirect(url_for('login'))
        elif not user.validate_password(request.form['password']):
            flash('ユーザ名とパスワードの組み合わせが間違っています')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    '''ログアウト用'''
    logout_user()
    return redirect(url_for('home'))
