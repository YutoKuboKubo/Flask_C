from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザー名が違います')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが違います')
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

    