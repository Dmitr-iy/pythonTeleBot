import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')

currency = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
    'тенге': 'KZT',
    'юань': 'CNY',
    'фунт': 'GBP',
    'франк': 'CHF',
    'сом': 'KGS',
    'йена': 'JPY',
    'биткоин': 'BTC',
    'лира': 'TRY',
    'драм': 'AMD',
    'реал': 'BRL',
    'рупий': 'INR',
}
