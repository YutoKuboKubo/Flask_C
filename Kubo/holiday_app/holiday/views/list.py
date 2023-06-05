from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/list')
def show_list():
    holiday = Holiday.query.all()
    return render_template('list.html', holiday=holiday)