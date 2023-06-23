from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_blog import db
from flask_blog.models.entries import User
from flask_blog.views.views import login_required

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    hantei=0
    if request.method == 'POST':
        reg_user = User.query.all()
        for r_g in reg_user:
            if request.form['username'] == r_g.username:
                hantei=1
                if request.form['password'] == r_g.password:
                    hantei=2
        if hantei == 0:
            flash('ユーザ名がありません')
            return redirect(url_for('show_entries'))
        elif hantei == 1:
            flash('パスワードが間違っています')
            return redirect(url_for('show_entries')) 
        else:                   
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))



#会員登録
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username1 = request.form.get('username')
        password1 = request.form.get('password')
        password_check = request.form.get('password1')
        #中身がなかったら返す
        if username1 == None or password1 == None:
            return render_template('register.html')
        #中身がなかったら返す
        if username1 == '' or password1 == '':
            flash('ユーザとパスワードを設定してください')
            return render_template('register.html')
        #パスワード確認用と一致
        if password1 != password_check :
            flash('パスワードが一致していません')
            return render_template('register.html')

        #既にあるユーザは登録しない
        reg_user = User.query.all()
        for r_u in reg_user:
            if str(username1) == str(r_u.username):
                flash('同じユーザが存在します。別のユーザで登録してください')
                return render_template('register.html')

    #Userのインスタンスを作成
        user = User(username=username1, password=password1)
        db.session.add(user)
        db.session.commit()
        flash('新規会員登録ありがとうございます')
        return redirect('login')
    else:
        return render_template('register.html')