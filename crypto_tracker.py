import requests
import pandas as pd
from datetime import datetime

# === Config ===
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

# === Fetch data ===
response = requests.get(url, params=params)

if response.status_code == 200:
    coins = response.json()
    data = []

    for coin in coins:
        data.append({
            "Name": coin["name"],
            "Symbol": coin["symbol"],
            "Price (USD)": coin["current_price"],
            "Market Cap": coin["market_cap"],
            "24h Change (%)": coin["price_change_percentage_24h"],
            "Volume (24h)": coin["total_volume"]
        })

    df = pd.DataFrame(data)

    # === Save to file with timestamp ===
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"crypto_prices_{today}.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved daily snapshot to: {filename}")
else:
    print("❌ Failed to fetch:", response.status_code)
