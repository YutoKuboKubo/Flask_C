from flask import request, redirect, url_for, render_template, flash, session
from app import app
from flask_login import (
    login_user, login_required, logout_user, current_user
)



@app.route('/')
def index():
    return render_template('index.html')