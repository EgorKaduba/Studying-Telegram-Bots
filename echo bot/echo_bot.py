from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "1111111111:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

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
    await message.reply(message.text)

# Другой метод регистрации хэндлеров (не нужно использовать декораторы)
# dp.message.register(process_start_command, Command(commands='start'))
# dp.message.register(process_help_command, Command(commands='help'))
# dp.message.register(send_echo)
if __name__ == "__main__":
    dp.run_polling(bot)
