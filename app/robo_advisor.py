# app/robo_advisor.py

import requests
import json

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

from datetime import datetime
now = datetime.now()

# Info Inputs

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
response = requests.get(request_url)
# print(type(response))
# print(response.status_code)
# print(response.text)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

date_keys = parsed_response["Time Series (Daily)"].keys()
dates = list(date_keys) # assumes first day is on top
latest_day = dates[0]
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]

high_prices = []

for date in dates:
    high_price = float(parsed_response["Time Series (Daily)"][date]["2. high"])
    high_prices.append(high_price)

recent_high = max(high_prices)

low_prices = []

for date in dates:
    low_price = float(parsed_response["Time Series (Daily)"][date]["3. low"])
    low_prices.append(low_price)

recent_low = min(low_prices)

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", now.strftime("%Y-%m-%d %I:%M%p"))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")