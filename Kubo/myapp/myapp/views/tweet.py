from flask import (
    request, redirect, url_for, render_template,
    flash, session
)
from myapp import app, db
from myapp.models.user import User, Tweets
from flask_login import login_required, current_user
from datetime import datetime


@app.route('/')
def home():
    tweets = Tweets.query.all()
    return render_template('home.html', tweets=tweets)


@app.route('/create_tweet', methods=['GET', 'POST'])
@login_required
def create_tweet():
    '''ツイート作成用'''
    if request.method == "POST":
        # # 画像をアップロードした場合
        # if request.files['picture_path'] == '':
        #     file = request.files['picture_path'].read()
        #     file_name = current_user.get_id() + '_' + str(int(datetime.now().timestamp())) + 'jpg'
        #     picture_path = 'myapp/static/tweet_images/' + file_name
        #     open(picture_path, 'wb').write(file)
        #     tweet_picture_path = 'tweet_images/' + file_name
        #     new_tweet = Tweets(request.form['title'], request.form['body'], tweet_picture_path, current_user.get_id())
        #     new_tweet.create_tweet()
        #     db.session.commit()
        # else:
        # ツイートを投稿したユーザを取得
        user = User.select_user_by_id(current_user.get_id())
        new_tweet = Tweets(request.form['title'], request.form['body'], None, user.id, user.username)
        new_tweet.create_tweet()
        db.session.commit()
        flash('ツイートの作成に成功しました')
        return redirect(url_for('home'))
    return render_template('create_tweet.html')


@app.route('/update_tweet/<int:id>', methods=['GET', 'POST'])
@login_required
def update_tweet(id):
    '''ツイート更新用'''
    tweet = Tweets.query.get(id)
    if request.method == 'POST':
        tweet.title = request.form['title']
        tweet.body = request.form['body']
        db.session.merge(tweet)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update_tweet.html', id=tweet.id)


@app.route('/delete_tweet/<int:id>')
@login_required
def delete_tweet(id):
    '''ツイート削除用'''
    tweet = Tweets.query.get(id)
    db.session.delete(tweet)
    db.session.commit()
    return redirect(url_for('home'))
