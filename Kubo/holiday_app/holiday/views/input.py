from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday

# input.htmlの処理
@app.route('/', methods=["GET", "POST"])
def input():
    if request.method == "POST":
        # レコードが存在しているか確認(データが無ければNone)
        exists = Holiday.query.get(request.form['holi_date'])
        # 押されたボタンの判定用変数
        value = request.form['button']
        # 新規登録・更新ボタンが押された場合
        if value == 'add':
            # あったら更新処理
            if exists:
                exists.holi_text = request.form['holi_text']
                db.session.merge(exists)
                db.session.commit()
                # 新規登録か判断する用のセッション
                session['status'] = 'update'
                # 入力された値を保存
                session['holi_date'] = request.form['holi_date']
                session['holi_text'] = request.form['holi_text']
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
        # 削除ボタンが押された場合
        elif value == 'delete':
            if exists:
                db.session.delete(exists)
                db.session.commit()
                # 新規登録か判断する用のセッション
                session['status'] = 'delete'
                session['holi_date'] = request.form['holi_date']
                session['holi_text'] = exists.holi_text
            else:
                flash(f"{request.form['holi_date']}は、祝日マスタに登録されていません")
                return redirect(url_for('input'))
        return redirect(url_for('result'))
    return render_template('input.html')
