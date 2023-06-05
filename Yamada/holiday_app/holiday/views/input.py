from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/maintenance_date', methods=['POST'])
def add_holiday():
    holiday = Holiday(
        holi_date=request.form['holiday'],
        holi_text=request.form['holiday_text']
    )
    db.session.add(holiday)
    db.session.commit()
    holi_date=request.form['holiday'],
    holi_text=request.form['holiday_text']
    return render_template('result.html', holi_date=holi_date, holi_text=holi_text)