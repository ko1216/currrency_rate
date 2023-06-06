import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
CURRENCY_RATES_FILE = 'currency_rates.json'


def get_currency_rate(base: str) -> float:
    """
    Получает курс от API и возвращает float
    :param base: str
    :return: float
    """

    url = "https://api.apilayer.com/exchangerates_data/latest"
    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data: dict) -> None:
    """
    Сохраняет данные в json файл.
    :param data: dict
    """
    with open(CURRENCY_RATES_FILE, 'a') as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATES_FILE) as f:
                data_list = json.load(f)
                data_list.append(data)
            with open(CURRENCY_RATES_FILE, 'w') as f:
                json.dump(data_list, f)
