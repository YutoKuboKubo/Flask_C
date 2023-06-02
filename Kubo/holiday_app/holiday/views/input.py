from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday


@app.route('/', methods=["GET", "POST"])
def new_holiday():
    if request.method == "POST":
        holiday = Holiday(
            holi_date=request.form['holi_date'],
            holi_text=request.form['holi_text']
        )
        db.session.add(holiday)
        db.session.commit()
        return redirect(url_for('result'))
    return render_template('input.html')


@app.route('/maintenance_date', methods=["GET"])
def result():
    return render_template('result.html')
