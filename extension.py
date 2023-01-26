import json
import requests
from config import currency


class ApiException(Exception):
    pass


class UnitConvert:
    @staticmethod
    def get_price(base: str, sym: str , amount: str):
        if base == sym:
            raise ApiException(f'Не возможно перевести одинаковые валюты {sym}.')
        try:
            base_curr = currency[base.lower()]
        except KeyError:
            raise ApiException(f'Не удалось обработать вашу валюту {base}')

        try:
            sym_curr = currency[sym.lower()]
        except KeyError:
            raise ApiException(f'Не удалось обработать вашу валюту {sym}')

        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'Не удалось обработать количество {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_curr}&tsyms={sym_curr}")
        total_price = json.loads(r.content)[currency[sym]]

        return total_price