import time
import logging
import requests


from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")


TOKEN = "TOKEN"
MSG = ("{}, будем смотреть гороскоп?\nНажми на кнопку Гороскоп и выбери знак зодиака.")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

#  создаем приветственное сообщение на команду старт


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет, {user_name}!")

    time.sleep(2)

    btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_gor = types.KeyboardButton('Гороскоп')
    btn_out = types.KeyboardButton('До встречи!')
    btns.add(btn_gor, btn_out)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)

@dp.message_handler(content_types=['text'])
async def url_handler(message: types.Message):
    if message.text == 'Гороскоп':
        keyboard = types.InlineKeyboardMarkup(row_width=4)
        buttons = [
            types.InlineKeyboardButton(
                "Овен", url="https://horoscopes.rambler.ru/aries/"),
            types.InlineKeyboardButton(
                "Телец", url="https://horoscopes.rambler.ru/taurus/"),
            types.InlineKeyboardButton(
                "Близнецы", url="https://horoscopes.rambler.ru/gemini/"),
            types.InlineKeyboardButton(
                "Рак", url="https://horoscopes.rambler.ru/cancer/"),
            types.InlineKeyboardButton(
                "Лев", url="https://horoscopes.rambler.ru/leo/"),
            types.InlineKeyboardButton(
                "Дева", url="https://horoscopes.rambler.ru/virgo/"),
            types.InlineKeyboardButton(
                "Весы", url="https://horoscopes.rambler.ru/libra/"),
            types.InlineKeyboardButton(
                "Скорпион", url="https://horoscopes.rambler.ru/scorpio/"),
            types.InlineKeyboardButton(
                "Стрелец", url="https://horoscopes.rambler.ru/sagittarius/"),
            types.InlineKeyboardButton(
                "Козерог", url="https://horoscopes.rambler.ru/capricorn/"),
            types.InlineKeyboardButton(
                "Водолей", url="https://horoscopes.rambler.ru/aquarius/"),
            types.InlineKeyboardButton(
                "Рыбы", url="https://horoscopes.rambler.ru/pisces/")
        ]
        keyboard.add(*buttons)
        await bot.send_message(message.from_user.id, "Гороскоп какого знака будем смотреть?", reply_markup=keyboard)
    if message.text == 'До встречи!':
        await bot.send_message(message.from_user.id, "Заходи снова. Пока!")
   

if __name__ == '__main__':
    executor.start_polling(dp)
