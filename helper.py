# import sqlite3
# import requests
# from newsapi.newsapi_client import NewsApiClient
# import collections



# DB_PATH = "news.db"
# current_date = dt.date.today
# newsapi = NewsApiClient(api_key="1ec0f2aedee24c70b1eecb0f97e30d26")

# def add_to_list(article):
#     try:
#         conn = sqlite3.connect(DB_PATH)
                       
#         # Once a connection has been established, we use the cursor
#         # object to execute queries
#         api_req = requests.get( "https://newsapi.org/v2/top-headlines?sources=engadget&apiKey=1ec0f2aedee24c70b1eecb0f97e30d26")
#         api_req = api_req.json()

#         extracted_articles = api_req["articles"]["source"]

#         c = conn.cursor()

#         for ex in extracted_articles:
#             article = ex["titles"]
#             DateViewed = current_date
#             sql = 'INSERT INTO news (article, DateViewed) VALUES(?,?)'
#             val = (article,DateViewed)
#             c.execute(sql,val)

#         # Keep the initial status as Not Started
        
        
#         conn.commit()
#         return {"article": article, "DateViewed": current_date}
#     except Exception as e:
#         print("Error: ", e)
#         return None
    

      
