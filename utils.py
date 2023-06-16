import json
import requests
from main import API_KEY


def get_currency_rate(currency: str) -> float:
    """Получает курс валюты от API и возвращает его в виде float"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    response = requests.get(url, headers={'apikey': API_KEY})
    response_data = json.loads(response.text)
    rate = response_data["rates"]["RUB"]
    return rate




