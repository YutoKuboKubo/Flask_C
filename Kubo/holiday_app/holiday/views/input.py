from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

# input.htmlの処理
@app.route('/', methods=["GET", "POST"])
def new_holiday():
    if request.method == "POST":
        holiday = Holiday(
            holi_date=request.form['holi_date'],
            holi_text=request.form['holi_text']
        )
        db.session.add(holiday)
        db.session.commit()
        # 入力された値を保存
        session['holi_date'] = request.form['holi_date']
        session['holi_text'] = request.form['holi_text']
        return redirect(url_for('result'))
    return render_template('input.html')

# result.htmlの処理（入力された値を表示する）
@app.route('/maintenance_date', methods=["GET"])
def result():
    # 入力された値を呼び出す
    holi_date = session.get('holi_date', None)
    holi_text = session.get('holi_text', None)
    # 値を渡す
    return render_template('result.html', holi_date=holi_date, holi_text=holi_text)
