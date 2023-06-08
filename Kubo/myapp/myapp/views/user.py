from flask import (
    request, redirect, url_for, render_template,
    flash, session
)
from myapp import app, db
from myapp.models.user import User, Tweets
from flask_login import login_required, current_user
from flask_bcrypt import generate_password_hash
from datetime import datetime


@app.route('/user/<int:id>', methods=['GET', 'POST'])
@login_required
def user(id):
    '''ユーザの情報変更用'''
    user = User.select_user_by_id(id)
    if request.method == "POST":
        user.username = request.form['username']
        user.password = generate_password_hash(request.form['password'])
        db.session.merge(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('user.html', id=id, username=user.username, password=user.password)
