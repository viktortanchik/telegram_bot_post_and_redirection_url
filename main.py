from aiogram import Bot, Dispatcher, executor
from aiogram import types
import asyncio
from aiogram.dispatcher.filters import Text

bot = Bot(token="2141799369:AAEhbbxAsNFkfeLs6kU4WYuz4i0O5iCzIyE")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("To change the post/message text, enter the command and write text >> example (/message_text  Hello world! )\n"
 "To change the button text, enter the command >> /button_text example (/button_text Tap to Win) \n"
 "To change the redirect link, enter the command   >> /name_url  (without /http (/name_url computernerd4090)\n" 
"To send a post  enter the command >> /post"
    )

@dp.message_handler(commands="button_text")
async def cmd_random(message: types.Message):
    print(message.text)
    file = open("txtButton.txt", "w")
    file.write(message.text[12:])
    file.close()

@dp.message_handler(commands="name_url")
async def cmd_random(message: types.Message):
    print(message.text[10:])
    file = open("name.txt", "w")
    file.write(message.text[10:])
    file.close()

@dp.message_handler(commands="message_text")
async def cmd_random(message: types.Message):
    print(message.text[14:])
    file = open("post.txt", "w")
    file.write(message.text[14:])
    file.close()

@dp.message_handler(commands="post")
async def cmd_random(message: types.Message):
    b = open("txtButton.txt", "r")
    Button_text = b.read()
    u = open("name.txt", "r")
    url = u.read()
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=Button_text, callback_data="value",url="https://t.me/"+url))#, callback_data="value"#@milancholiac
    filer = open("post.txt", "r")
    str = filer.read()
    filer.close()
    b.close()
    u.close()
    await bot.send_message(-1001600149738, str,reply_markup=keyboard)#test_pots_pip  -1001600149738   # test_chat -1001392919876


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)