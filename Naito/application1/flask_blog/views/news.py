import requests
from bs4 import BeautifulSoup
import re
import pandas as pd





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

df = pd.DataFrame(zip(title,url,date), columns = ['title', 'url', 'date'])
print(df.title[0])




