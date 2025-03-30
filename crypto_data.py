import requests
from config import COINGECKO_URL, HISTORICAL_URL, CRYPTO_LIST

def get_crypto_prices():
    """Fetch real-time crypto prices."""
    params = {"ids": ",".join(CRYPTO_LIST), "vs_currencies": "usd", "include_market_cap": "true"}
    response = requests.get(COINGECKO_URL, params=params)
    return response.json()

def get_historical_data(crypto_id):
    """Fetch historical crypto price trends."""
    url = HISTORICAL_URL.format(crypto_id)
    params = {"vs_currency": "usd", "days": "7", "interval": "daily"}
    response = requests.get(url, params=params)
    return response.json()
