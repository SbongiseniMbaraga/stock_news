import requests

#get stock data
stock_api_key = "HYH8K48YPWAAFQFT"
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=5min&apikey={stock_api_key}"

response = requests.get(url=stock_url)
print(response.json())