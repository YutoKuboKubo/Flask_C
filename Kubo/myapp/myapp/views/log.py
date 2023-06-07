from flask import (
    request, redirect, url_for, render_template,
    flash, session
)
from myapp import app
from myapp.models.user import User
from flask_login import (
    login_user, login_required, logout_user, current_user
)


@app.route('/login')
def index():
    return render_template('index.html')