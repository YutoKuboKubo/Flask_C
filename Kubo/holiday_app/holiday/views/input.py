from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
from holiday.lib.func import keep_session, validate_date, validate_text


# input.htmlの処理
@app.route('/', methods=["GET", "POST"])
def input():
    if request.method == "POST":
        # 日付のバリデーション
        if validate_date(request.form['holi_date']):
            return redirect(url_for('input'))
        # レコードが存在しているか確認(データが無ければNone)
        exists = Holiday.query.get(request.form['holi_date'])
        # 押されたボタンの判定用変数
        value = request.form['button']
        # 新規登録・更新ボタンが押された場合
        if value == 'add':
            # テキストのバリデーション
            if validate_text(request.form['holi_text']):
                return redirect(url_for('input'))
            # あったら更新処理
            if exists:
                exists.holi_text = request.form['holi_text']
                db.session.merge(exists)
                db.session.commit()
                # セッションに保存
                keep_session('update', request.form['holi_date'], request.form['holi_text'])
            else:
                # 新しいレコードを追加
                holiday = Holiday(
                    holi_date=request.form['holi_date'],
                    holi_text=request.form['holi_text']
                )
                db.session.add(holiday)
                db.session.commit()
                # セッションに保存
                keep_session('add', request.form['holi_date'], request.form['holi_text'])

        # 削除ボタンが押された場合
        elif value == 'delete':
            if exists:
                db.session.delete(exists)
                db.session.commit()
                # セッションに保存
                keep_session('delete', request.form['holi_date'], exists.holi_text)

            else:
                flash(f"{request.form['holi_date']}は、祝日マスタに登録されていません")
                return redirect(url_for('input'))
        return redirect(url_for('result'))
    return render_template('input.html')
