from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/maintenance_date', methods=['POST'])
def input_holiday():
    if request.form["button"] == "add_holiday":
        holiday = Holiday(
            holi_date=request.form['holiday'],
            holi_text=request.form['holiday_text']
        )
        holi_date=request.form['holiday']
        holi_text=request.form['holiday_text']
        exists = Holiday.query.get(holi_date)
        if exists:
            db.session.merge(holiday)
            db.session.commit()
            return render_template('result.html', holi_date=holi_date, holi_text=holi_text, tag="update")
        else:
            db.session.add(holiday)
            db.session.commit()
            return render_template('result.html', holi_date=holi_date, holi_text=holi_text, tag="registar")

    elif request.form["button"] == "delete_holiday":
        holi_date=request.form['holiday']
        holiday = Holiday.query.get(holi_date)
        holi_text = holiday.holi_text
        db.session.delete(holiday)
        db.session.commit()
        return render_template('result.html', holi_date=holi_date, holi_text=holi_text, tag="delete")