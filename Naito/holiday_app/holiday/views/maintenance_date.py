
from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.mst_holiday import Holiday
from datetime import datetime

@app.route('/maintenance_date',methods=['POST'])
def maintenance():
    
    #string型からdate型に変換   
    date_time = datetime.strptime(request.form['holiday'], '%Y-%m-%d')
    #DBデータの取得
    holiday = Holiday.query.filter_by(holi_date=date_time).first() 
    if request.form['button'] == 'insert_update':
        
        #入力チェック（日付・テキスト）
        if request.form['holiday'] == '' or request.form['holiday_text'] == '':
            flash('日付・テキストを入力してください')
            return render_template('input.html')
        
        if len(request.form['holiday_text']) >= 20:
            flash('テキストは20文字以内で入力してください')
            return render_template('input.html')
        
        #新規登録
        if holiday is None:
            #インスタンスの作成
            h_db=Holiday(holi_date=date_time,holi_text=request.form['holiday_text'])
            db.session.add(h_db)
            db.session.commit()
            message= f"{str(date_time)[:11]}({request.form['holiday_text']})が登録されました"

        #更新
        else:
            #インスタンスの作成
            #同じテキストが存在した場合
            if holiday.holi_text == request.form['holiday_text']:
                flash(f"{holiday.holi_date}{holiday.holi_text}は、すでに登録されています" )
                return render_template('input.html')
            
            h_db=Holiday(holi_date=date_time,holi_text=request.form['holiday_text'])
            db.session.merge(h_db)
            db.session.commit()
            message =  f"{str(date_time)[:11]}は、{request.form['holiday_text']}に更新されました"

        return render_template('result.html',message=message)

    #削除
    elif request.form["button"] == "delete":
        #入力チェック（日付・テキスト）
        if request.form['holiday'] == '':
            flash('日付を入力してください')
            return render_template('input.html')
        
        #存在した場合のみ削除
        if holiday is None: 
            flash(request.form["holiday"] + "は、祝日マスタに登録されていません")
            return redirect(url_for("input")) 
        else:
            
            message = f"{holiday.holi_date}{holiday.holi_text}は、削除されました"   
            Holiday.query.filter_by(holi_date = date_time).delete()
            db.session.commit()           
            return render_template("result.html", message = message)     