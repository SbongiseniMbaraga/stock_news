import requests
from twilio.rest import Client
import get_stock_data

# gets the relevant news
title_description = ""

def data():
    global title_description
    news_api_key = "c8510367ea5842fcb7ad80cadded9056"
    news_url = f"https://newsapi.org/v2/everything?q=Tesla&apiKey={news_api_key}"
    response = requests.get(url=news_url)
    news_data = response.json()

    #get news data
    article_data = news_data["articles"]
    for item in article_data:
        article_title = item["title"]
        article_description = item["description"]
        title_description = f"TITLE: {article_title}\n\nDESCRIPTION: {article_description}\n\n\n"

    account_sid = "ACf6fece104e06565ec1d2e2e9471d437a"
    auth_token = "6a3f5e97306c10b116024f587c6f5707"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f"\n{get_stock_data.print_stock_data()}{title_description}",
            from_="+18647124113",
            to="+27823956607"
        )

    print(message.sid)