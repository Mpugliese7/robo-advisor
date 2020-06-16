# app/robo_advisor.py

import csv
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

from datetime import datetime
now = datetime.now()

# Info Inputs

ticker = input("Please input a ticker: ")
if not ticker.isalpha():
    raise ValueError("Error: Please enter a valid stock ticker like WFC")
if len(ticker) > 5:
    raise ValueError("Error: Please enter a valid stock ticker like WFC")

api_key = os.environ.get("ALHPAADVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"
response = requests.get(request_url)

parsed_response = json.loads(response.text)

if "Error Message" in parsed_response:
    raise ValueError("Sorry, couldn't find any trading data for that stock ticker")

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

date_keys = parsed_response["Time Series (Daily)"].keys()
dates = list(date_keys) # assumes first day is on top
latest_day = dates[0]
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = float(parsed_response["Time Series (Daily)"][date]["2. high"])
    low_price = float(parsed_response["Time Series (Daily)"][date]["3. low"])
    high_prices.append(high_price)
    low_prices.append(low_price)

recent_high = max(high_prices)
recent_low = min(low_prices)

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        daily_prices = parsed_response["Time Series (Daily)"][date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
        })

if float(latest_close) < 1.2 * float(recent_low): 
    recommendation = "Buy!"
else:
    recommendation = "Don't Buy!"

if recommendation == "Buy!":
    recommendation_reason = "Because the stock's latest close is within 20% of its recent low"
else:
    recommendation_reason = "Because the stock's latest close is not within 20% of its recent low"

print("-------------------------")
print(f"SELECTED SYMBOL: {ticker}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", now.strftime("%Y-%m-%d %I:%M%p"))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {recommendation}")
print(f"RECOMMENDATION REASON: {recommendation_reason}")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")