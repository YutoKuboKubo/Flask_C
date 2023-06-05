from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/list')
def list_holiday():
    return render_template('list.html')