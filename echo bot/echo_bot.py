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


@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Данный тип не поддерживается")


if __name__ == "__main__":
    dp.run_polling(bot)
