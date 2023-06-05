from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
import datetime

@app.route("/maintenance_date", methods = ["POST"])
def maintenance_date():
    datetime_str = request.form["holiday"]
    holiday_name = request.form["holiday_text"]

# check
    if holiday_name == '':
        flash("祝日テキストが未入力です")
        return redirect(url_for('input'))
    elif len(holiday_name) > 20:
        flash('祝日テキストは20字以内で入力してください')
        return redirect(url_for('input'))
    elif datetime_str == '':
        flash("日付が未入力です")
        return redirect(url_for('input'))
    
    dt = datetime.datetime.strptime(datetime_str, '%Y-%m-%d') # date型に変換
    holiday = Holiday.query.filter_by(holi_date = dt).first()

# add /update
    if request.form["button"] == "holiday_update":
        if holiday:
            holiday_input = Holiday(holi_date = holiday.holi_date, holi_text = holiday_name)  
            db.session.merge(holiday_input)
            db.session.commit()
            message = holiday_name + "は「" + holiday_name + "」に更新されました"
        else:
            holiday_input = Holiday(holi_date = dt, holi_text = holiday_name)  
            db.session.add(holiday_input)
            db.session.commit()
            message = holiday_name + "が登録されました"
        return render_template("result.html", message = message)

# delete
    elif request.form["button"] == "holiday_delete":
        if holiday: 
            message = str(holiday.holi_date) + holiday.holi_text + "は、削除されました"              
            Holiday.query.filter_by(holi_date = dt).delete()
            db.session.commit()
            return render_template("result.html", message = message) 
        else:
            flash(holiday_name + "は、祝日マスタに登録されていません")
            return redirect(url_for("input"))