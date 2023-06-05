from flask import request, redirect, url_for, render_template, flash, session
from holiday import app

@app.route('/back')
def back():
    return redirect(url_for("show_entries"))