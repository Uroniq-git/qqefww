from typing import Type

import aiogram
from main import *
from aiogram import Bot, Dispatcher, executor, types
import config

def isAdmin(message: types.Message):
    if message.from_user.id == config.ADMIN_ID:
        return True
    else:
        return False

async def addChatToDB(message: types.Message):
    sql = f"SELECT * FROM chats WHERE chat_id={message.chat.id}"
    cursor.execute(sql)
    chat = cursor.fetchall()
    if chat:
        pass
    else:
        cursor.execute(f"INSERT INTO chats VALUES ({message.chat.id})")
        conn.commit()


async def getAllChats():
    sql = f"SELECT * FROM chats"
    chats = cursor.execute(sql)
    return chats