import telebot
from telebot import types
import random
import datetime

token = "2108949376:AAEPQGM8R2JAOOqJtjYCP1cG5bo_lmF6CNQ"

bot = telebot.TeleBot(token)


def date():
    today = datetime.datetime.today()
    year = today.year
    day = today.day
    month = today.month
    hour = today.hour
    minute = today.minute

    months = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря'
    }

    tx_month = months[str(month)]
    return f'Сегодня {day} {tx_month} {year} года, {hour}:{minute}'


anek = [
    "Журналист берет интервью у старца 145 лет:\n- Скажите, в чем секрет Вашей долгожительности?\n- Да нет ни какого "
    "секрета, за свю свою жизнь я ни когда ни с кем не спорил.\n- Да ладно, не может такого быть!\n- Ну не может, "
    "так не может...",

    "Как называется загородный дом, в котором допрашивают людей?\n\n\nДача показаний",

    "Штирлиц шагал по Берлину. Ничто не выдавало в нём разведчика, кроме советских орденов на груди, будёновки на "
    "голове и парашюта, волочившегося следом."
]


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Сайт МТУСИ", "/help", "Анекдот", "Дата")
    bot.send_message(message.chat.id, 'Привет! Чтобы узнать команды, используй команду /help', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n '
                                      '-Рассказывать анекдоты: "Анекдот"\n '
                                      '-Отправлять ссылку на официальный сайт МТУСИ: "Сайт МТУСИ"\n '
                                      '-Говорить точную дату: "Дата"')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "сайт мтуси":
        bot.send_message(message.chat.id, 'Тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "анекдот":
        bot.send_message(message.chat.id, random.choice(anek))
    elif message.text.lower() == "дата":
        bot.send_message(message.chat.id, date())
    else:
        bot.send_message(message.chat.id, 'Такой команды нет! /help')


bot.polling(non_stop=True)
