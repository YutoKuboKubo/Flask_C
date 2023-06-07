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

@app.route('/login')
def login():
    return render_template('login.html')


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