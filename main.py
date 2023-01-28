import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
import requests
from grabber import grab_vi

API_TOKEN = '5812705690:AAH4j051brpon7ErGWA4eKgtSGX-0TEKbA0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Send me the link of any youtube video and i will return its thumbnail!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    if grab_vi(message.text) == 1:
        await message.reply("Invalid URL")
    else:
        await message.reply("Processing...")
        p = requests.get(f'https://img.youtube.com/vi/{grab_vi(message.text)}/maxresdefault.jpg')
        out = open("img.jpg", "wb")
        out.write(p.content)
        out.close()
        await bot.send_photo(message.from_id,  photo=InputFile("img.jpg"))
        os.remove("img.jpg")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
