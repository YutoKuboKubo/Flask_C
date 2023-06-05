from flask import request, redirect, url_for, render_template, flash, session
from holiday import app

# result.htmlの処理（入力された値を表示する）
@app.route('/maintenance_date', methods=["GET"])
def result():
    # 入力された値を呼び出す
    holi_date = session.get('holi_date', None)
    holi_text = session.get('holi_text', None)
    status = session.get('status', None)
    # 値を渡す
    return render_template('result.html', holi_date=holi_date, holi_text=holi_text, status=status)
