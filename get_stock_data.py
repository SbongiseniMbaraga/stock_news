import requests
from datetime import datetime, timedelta

#get stock data
stock_api_key = "HYH8K48YPWAAFQFT"
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={stock_api_key}"
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=HYH8K48YPWAAFQFT
response = requests.get(url=stock_url)
stock_data = response.json()

#step one: pull yesterdays closing price then pull closing data for previous day
closing_date_yesterday = 0
closing_date_previous_to_yesterday = 0

def print_stock_data():
    global closing_date_yesterday
    global closing_date_previous_to_yesterday

    stock_date_data = stock_data["Time Series (Daily)"]
    yesterday = datetime.now() - timedelta(1)
    formatted_yesterday_date = datetime.strftime(yesterday, "%Y-%m-%d")

    previous_to_yesterday = datetime.now() - timedelta(2)
    formatted_previous_date = datetime.strftime(previous_to_yesterday, "%Y-%m-%d")

    for stock_date in stock_date_data:
        date_of_stock = stock_date_data[stock_date]
        closing_price = date_of_stock["4. close"]

        #gets yesterdays stock data
        if stock_date == formatted_yesterday_date:
            closing_date_yesterday = closing_price

        #gets previous days date
        if stock_date == formatted_previous_date:
            closing_date_previous_to_yesterday = closing_price

    difference = float(closing_date_previous_to_yesterday) - float(closing_date_yesterday)

    yesterdays_closing_price = float(closing_date_yesterday)
    previous_to_yesterday_closing_price = float(closing_date_previous_to_yesterday)

    if difference < 0:
        get_percentage_decrease(yesterdays_closing_price, previous_to_yesterday_closing_price)
    else:
        get_percentage_increase(yesterdays_closing_price, previous_to_yesterday_closing_price)

def get_percentage_increase(yesterdays_closing_price, previous_to_yesterday_closing_price):
    increase = 100 * (round(yesterdays_closing_price) - round(previous_to_yesterday_closing_price)) / round(previous_to_yesterday_closing_price)
    return print(f"The Stock Price increased by {round(increase)}%")

def get_percentage_decrease(yesterdays_closing_price, previous_to_yesterday_closing_price):
    increase = -100 * (round(yesterdays_closing_price) - round(previous_to_yesterday_closing_price)) / round(previous_to_yesterday_closing_price)
    return print(f"The Stock Price fell by {round(increase - increase - increase)}%")