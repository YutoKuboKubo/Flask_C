from flask import request, redirect, url_for, render_template, flash, session
from app import app



@app.route('/')
def index():
    return render_template('index.html')