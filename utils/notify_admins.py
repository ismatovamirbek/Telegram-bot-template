import logging
import asyncio
from aiogram import Dispatcher
from data.config import ADMINS

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            message = await dp.bot.send_message(admin, "Bot ishga tushdi")  # Send a message
            await asyncio.sleep(5)  # Wait for 5 seconds
            await dp.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)  # Delete message

        except Exception as err:
            logging.exception(err)  # Log the error properly

