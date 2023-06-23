import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_blog import db
from flask_blog.models.entries import News
from flask_blog.views.views import login_required

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

@app.route('/news',methods=['GET','POST'])
def News():

    # ヤフーニュースの情報を取得する
    URL = "https://news.yahoo.co.jp/search?p=%E3%83%9E%E3%82%A4%E3%83%8A%E3%83%93&ei=utf-8"
    rest = requests.get(URL)

    # BeautifulSoupにヤフーニュースのページ内容を読み込ませる
    soup = BeautifulSoup(rest.text, "html.parser")

    title = []
    url =[]
    date=[]
    # ヤフーニュースの見出しとURLの情報を取得して出力する
    #見出し
    text_list = soup.find_all(class_='newsFeed_item_title')
    for data in text_list:
        title.append(data.contents)

    #URL
    url_list = soup.find_all(class_='sc-kDdnqA cBcECR newsFeed_item_link')
    for data1 in url_list:
        url.append(data1.attrs['href'])

    #日付
    day = soup.find_all(class_='newsFeed_item_date')
    for data2 in day:
        date.append(data2.contents)

    df = pd.DataFrame(zip(title,url,date), columns = ['title1', 'url1', 'date1'])

    for i in range(len(title)):
        #Userのインスタンスを作成
        user = News(title=df.title1[i], url=df.url1[i], date=df.date1[i])
        db.session.add(user)
        db.session.commit()
    n = News.query.all()
    return render_template('news.html',news_list=n)

    



