# crypto-price-tracker
This Python script uses the CoinGecko API to fetch real-time data for the top 10 cryptocurrencies. It captures name, symbol, price, market cap, 24h change, and volume, then saves it to a timestamped CSV using pandas. Ideal for automation, financial monitoring, or data tracking with no API key required.

## Features
- Fetches live market data (name, symbol, price, volume, market cap, 24h change)
- Saves daily snapshots as `crypto_prices_YYYY-MM-DD.csv`
- Ideal for daily monitoring or integration with dashboards

## Technologies Used
- Python 3
- `requests` for API calls
- `pandas` for data handling
- CoinGecko API (no API key required)

## Sample Output
| Name    | Symbol | Price (USD) | Market Cap | 24h Change (%) | Volume (24h) |
|---------|--------|-------------|-------------|----------------|--------------|
| Bitcoin | btc    | 108668.00   | 2.16T       | 0.34           | ...          |

## How to Use
1. Install dependencies:
```bash
pip install pandas requests
