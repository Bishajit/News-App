from flask import Flask, render_template, request, Response
from newsapi.newsapi_client import NewsApiClient
import requests, sqlite3
import datetime as dt





application = app = Flask(__name__)

 
@app.route('/')
def Index():

    newsapi = NewsApiClient(api_key="1ec0f2aedee24c70b1eecb0f97e30d26")
    topheadlines = newsapi.get_top_headlines(sources="engadget")

    articles = topheadlines['articles']
 
    img = []
    auth = []
    desc = []
    name = []
    website = []
    pub = []
    con =[]



    for i in range(len(articles)):
        myarticles = articles[i]

        
        img.append(myarticles['urlToImage'])
        auth.append(myarticles["author"])
        name.append(myarticles['title'])
        desc.append(myarticles['description'])
        website.append(myarticles["url"])
        pub.append(myarticles["publishedAt"])
        con.append(myarticles["content"])
 
 
 
    mylist = zip(img, auth, name, desc, website, pub, con)
 
 
    return render_template('index.html', context = mylist)

DB_PATH = "news.db"


conn = sqlite3.connect(DB_PATH)


api_req = requests.get("https://newsapi.org/v2/top-headlines?sources=engadget&apiKey=1ec0f2aedee24c70b1eecb0f97e30d26")
api_req = api_req.json()
extracted_articles = api_req["articles"]
current_date = dt.date.today()

c = conn.cursor()

for ex in extracted_articles:
    article = ex['title']
    date_viewed = current_date
    sql = 'INSERT OR IGNORE INTO News(article,date_viewed) VALUES(?,?)'
    val = (article, date_viewed)
    c.execute(sql,val)
    

conn.commit()


if __name__ == "__main__":
    app.run(debug=True)