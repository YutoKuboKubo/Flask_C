from flask import session, flash, redirect, url_for
from datetime import datetime

def keep_session(status, holi_date, holi_text):
    # 新規登録か判断する用のセッション
    session['status'] = status
    # 入力された値を保存
    session['holi_date'] = holi_date
    session['holi_text'] = holi_text


# 日付のバリデーション
def validate_date(holi_date):
    try:
        datetime.strptime(holi_date, '%Y-%m-%d')
        return False
    except:
        flash('日付を入力してください')
        return True


# テキストのバリデーション
def validate_text(holi_text):
    if holi_text == '':
        flash('テキストを入力してください')
        return True
    elif len(holi_text) > 20:
        flash('テキストは20文字以内で入力してください')
        return True
    return False
