import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = ''
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu Alaykum Wikipedia botda Xush kelibsiz\n Istalgan mavzuda malumot axtarishingiz mumkin")
@dp.message_handler(commands=[ 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Tez orada siz bilan Aperatorlarimiz bolg'lanishadi\n Iltimos kuting")

@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await  message.answer(respond)
    except:
        await message.answer("bu mavzuga oid malumot topilmadi \n boshqa nom bilan qidiring")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
