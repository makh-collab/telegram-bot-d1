import logging
import asyncio
from config import token
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart

bot=Bot(token=token)
logging.basicConfig(level=logging.INFO)
dis=Dispatcher()

@dis.message(CommandStart())
async def startbot(message=Message):
    await message.answer('Assalomu aleykum, botga xush kelibsiz!')
    

async def main():
    await dis.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main()) 






# @dis.message(CommandStart())
# async def Startbot(message: Message):
#     u_id=message.from_user.id
#     un=message.from_user.username
#     fn=message.from_user.first_name
#     ln=message.from_user.last_name
#     l=message.from_user.language_code
#     b=message.from_user.is_bot
#     pre=message.from_user.is_premium
#     await
# bot.send_message(chat_id=)