from flask import Flask, render_template, request, Response
from newsapi.newsapi_client import NewsApiClient #from newsapi import NewsAPiClient sometimes doesnt work
import requests, sqlite3
import datetime as dt





application = app = Flask(__name__) #wont run if its app.py

 
@app.route('/') #routes to the link
def Index():

    newsapi = NewsApiClient(api_key="1ec0f2aedee24c70b1eecb0f97e30d26")
    topheadlines = newsapi.get_top_headlines(sources="engadget")

    #Goes to the api and takes everything from articles 
    articles = topheadlines['articles']
    
    #saves all these variables to a empty list
    img = []
    auth = []
    name = []
    desc = []
    website = []
    pub = []
    
    #This for loop iterates so it fills these variables with the data from the api.
    for i in range(len(articles)):
        myarticles = articles[i]

        
        img.append(myarticles['urlToImage'])
        auth.append(myarticles["author"])
        name.append(myarticles['title'])
        desc.append(myarticles['description'])
        website.append(myarticles["url"])
        pub.append(myarticles["publishedAt"])
 
 
 
    mylist = zip(img, auth, name, desc, website, pub)
 
 
    return render_template('index.html', context = mylist)


#Index method ends and next, save the data to the database 

DB_PATH = "news.db" #path to database


conn = sqlite3.connect(DB_PATH) #sqlite connects to the database


api_req = requests.get("https://newsapi.org/v2/top-headlines?sources=engadget&apiKey=1ec0f2aedee24c70b1eecb0f97e30d26") #
api_req = api_req.json() #gets the information and turns it into json
extracted_articles = api_req["articles"] #Gets everything underneath articles
current_date = dt.date.today() #Uses datetime module to set dt to the current day

c = conn.cursor()

for ex in extracted_articles:
    article = ex['title']
    date_viewed = current_date
    sql = 'INSERT OR IGNORE INTO News(article,date_viewed) VALUES(?,?)' # Without the ignore it will just keep repeating the headline for the day everytime you click on the link
    val = (article, date_viewed)
    c.execute(sql,val)
    

conn.commit()


if __name__ == "__main__":
    app.run(debug=True)