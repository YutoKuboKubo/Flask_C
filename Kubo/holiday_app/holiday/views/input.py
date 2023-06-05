from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

# input.htmlの処理
@app.route('/', methods=["GET", "POST"])
def new_holiday():
    if request.method == "POST":
        # レコードが存在しているか確認(データが無ければNone)
        exists = Holiday.query.get(request.form['holi_date'])
        # あったら更新処理
        if exists:
            exists.holi_text = request.form['holi_text']
            db.session.merge(exists)
            db.session.commit()
            # 新規登録か判断する用のセッション
            session['status'] = 'update'
        else:
            # 新しいレコードを追加
            holiday = Holiday(
                holi_date=request.form['holi_date'],
                holi_text=request.form['holi_text']
            )
            db.session.add(holiday)
            db.session.commit()
            # 新規登録か判断する用のセッション
            session['status'] = 'add'
        # 入力された値を保存
        session['holi_date'] = request.form['holi_date']
        session['holi_text'] = request.form['holi_text']
        return redirect(url_for('result'))
    return render_template('input.html')
