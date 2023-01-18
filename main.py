from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = ''


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Отправить фоточки!', url='https://tally.so/r/me5yLk')
urlkb.add(urlButton)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    with open('photo_2023-01-09_15-16-47.jpg', 'rb') as file:
        await message.answer_photo(file)
    await message.answer("Привет! \n\
С помощью нашего сервиса ты сможешь отправить распечатанные фотографии к себе домой. С тебя - выбрать пять твоих лучших фотографий, с нас - все остальное :)\n\n\
*5 фотографий* на сатиновой бумаге + отправка твоим близким - *600₽* \n\
Отправим за 1-2 дня и вышлем тебе трек-номер для отслеживания. ", reply_markup=urlkb, parse_mode="Markdown")


@dp.message_handler(commands=['new'])
async def process_start_command(message: types.Message):
    with open('photo_2023-01-09_13-51-04.jpg', 'rb') as file:
        await message.answer_photo(file)
    await message.answer("Отправить ещё фоточек? Без проблем :) \n\n\
*5 фотографий* на сатиновой бумаге + отправка твоим близким - *600₽* \n\n \
Отправим за 1-2 дня и вышлем тебе трек-номер для отслеживания.", reply_markup=urlkb, parse_mode="Markdown")

@dp.message_handler(commands=['support'])
async def process_help_command(message: types.Message):
    await message.answer("Переходи в наш чат с поддержкой, мы рады помочь тебе! @quack_qryack\n\
Если у тебя есть предложения, мы готовы к сотрудничеству. У нас еще много интересных проектов ;)")

if __name__ == '__main__':
    executor.start_polling(dp)