from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "7789376752:AAEAMrfrCmnH20p82wrG7P7gThVvkjhAd64"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer("Привет!\nМеня зовут Егор\nНапиши мне что-нибудь")


@dp.message(Command(commands=['help']))
async def bot_help(message: Message):
    await message.answer("Напиши мне что-нибудь и в ответ я пришлю тебе твоё сообщение")


async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


async def send_echo(message: Message):
    await message.reply(message.text)


# Другой метод регистрации хэндлеров (не нужно использовать декораторы)
# dp.message.register(start, Command(commands='start'))
# dp.message.register(bot_help, Command(commands='help'))
# dp.message.register(send_echo)
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)
if __name__ == "__main__":
    dp.run_polling(bot)
