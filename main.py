
import telebot
from config import TOKEN, currency
from extension import ApiException, UnitConvert


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def begin(message: telebot.types.Message):
    text = 'Добро пожаловать в конвертор валюты! \
Чтобы начать работу введите команду: /help'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def instructions(message: telebot.types.Message):
    text = 'Чтобы начать конвертацию введите команду: \n"наименование валюты"  \
"в какую валюту перевести"  \
"количество переводимой валюты"\n Для просмотра списка всех доступных валют введите команду: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'

    for i in currency.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    prise = message.text.split(' ')
    try:
        if len(prise) !=3:
            raise ApiException('Не верное количество параметров!')

        base, sym, amount = prise
        total_sym = UnitConvert.get_price(base, sym, amount)
    except ApiException as  e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} в {sym} - {total_sym}'
        bot.send_message(message.chat.id, text)


bot.polling()