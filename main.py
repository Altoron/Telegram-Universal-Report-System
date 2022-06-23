import logging, time
from colorama import init
init()
from colorama import Fore, Back, Style
from aiogram import Bot, Dispatcher, executor, types
#token from botfather
API_TOKEN = '5517050003:AAHGPzI3Qbx6DS_OOFRdBc5UMT4C_CBPwA8'
#id of person who recive reports
ownerid = 2136916358
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#start message
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.answer("Hello!\nThis is universal reporter!\nby .")

#recive report
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    #console print
    print(Fore.YELLOW + "\n \n###\n(New Report) > \n" + Fore.WHITE + "===\n" + message.text + "\n===" + Fore.GREEN + "\nfrom user {@" + message.from_user.username + "}" + "\n[" + time_string+ "]" + Fore.WHITE)
    #client answer
    await message.answer("Thank you for report\nIf we would have some quastions for you we send you massage\nHave a nice day!")
    #send report to owner
    await bot.send_message(ownerid, "(New Report) > \n" + "===\n" + message.text + "\n===" + "\nfrom user {@" + message.from_user.username + "}" + "\n " + time_string)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
