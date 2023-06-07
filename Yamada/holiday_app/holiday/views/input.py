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
        holi_date=request.form['holiday']
        holi_text=request.form['holiday_text']
        if holi_date == "":
            flash('日付が未入力です。入力してください。')
            return redirect(url_for("show_entries"))
        elif holi_text == "":
            flash('テキストが未入力です。入力してください。')
            return redirect(url_for("show_entries"))
        elif len(holi_text) > 10:
            flash('テキストは20文字以下で入力してください。')
            return redirect(url_for("show_entries"))
        else:
            holiday = Holiday(
                holi_date=request.form['holiday'],
                holi_text=request.form['holiday_text']
            )
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
        if holi_date == "":
            flash('日付が未入力です。入力してください。')
            return redirect(url_for("show_entries"))
        else:
            exists = Holiday.query.get(holi_date)
            if exists:
                holiday = Holiday.query.get(holi_date)
                holi_text = holiday.holi_text
                db.session.delete(holiday)
                db.session.commit()
                return render_template('result.html', holi_date=holi_date, holi_text=holi_text, tag="delete")
            else:
                flash('{0}は、祝日マスタに登録されていません'.format(holi_date))
                return redirect(url_for("show_entries"))