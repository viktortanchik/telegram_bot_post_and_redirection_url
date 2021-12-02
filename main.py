from aiogram import Bot, Dispatcher, executor
from aiogram import types
import asyncio
from aiogram.dispatcher.filters import Text

bot = Bot(token="2141799369:AAEhbbxAsNFkfeLs6kU4WYuz4i0O5iCzIyE")
dp = Dispatcher(bot)

userid = 674868256
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    print(message['from'].id)
    if message['from'].id == userid:
        await message.answer("To change the post/message text, enter the command and write text >> example (/message_text  Hello world! )\n"
     "To change the button text, enter the command >> /button_text example (/button_text Tap to Win) \n"
     "To change the redirect link, enter the command   >> /name_url  (without /http (/name_url computernerd4090)\n" 
    "To send a post  enter the command >> /post\n"
    "To change the chat where the message should post  "
    "Follow the next step. Use this bot to receive an ID of your chat/channel Then use command /change_id >> example ( /change_id -123456789 ) ( @username_to_id_bot )"
        )
    else:
        await message.answer("Access closed!")


@dp.message_handler(commands="button_text")
async def cmd_random(message: types.Message):
    if message['from'].id == userid:
        print(message.text)
        file = open("txtButton.txt", "w")
        file.write(message.text[12:])
        file.close()

@dp.message_handler(commands="name_url")
async def cmd_random(message: types.Message):
    if message['from'].id == userid:
        print(message.text[10:])
        file = open("name.txt", "w")
        file.write(message.text[10:])
        file.close()

@dp.message_handler(commands="message_text")
async def cmd_random(message: types.Message):
    if message['from'].id == userid:
        print(message.text[14:])
        file = open("post.txt", "w")
        file.write(message.text[14:])
        file.close()

@dp.message_handler(commands="chat_id")
async def cmd_random(message: types.Message):
    if message['from'].id == userid:
        print(message.text[9:])
        file = open("chat_id.txt", "w")
        file.write(message.text[9:])
        file.close()

@dp.message_handler(commands="post")
async def cmd_random(message: types.Message):
    if message['from'].id == userid:
        b = open("txtButton.txt", "r")
        Button_text = b.read()
        u = open("name.txt", "r")
        url = u.read()
        c = open("chat_id.txt", "r")
        chat_id = c.read()
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text=Button_text, callback_data="value",url="https://t.me/"+url))#, callback_data="value"#@milancholiac
        filer = open("post.txt", "r")
        str = filer.read()
        filer.close()
        b.close()
        u.close()
        c.close()
        await bot.send_message(chat_id, str,reply_markup=keyboard)#test_pots_pip  -1001600149738   # test_chat -1001392919876
#-1001600149738

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)