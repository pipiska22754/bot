from telethon import TelegramClient
from telethon.sessions import StringSession
from config import API_ID, API_HASH, PHONE, GROUPS
import asyncio

async def send_mailing(message: str):
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        code = input("Введите код: ")
        await client.sign_in(PHONE, code)
    
    for chat_id in GROUPS:
        try:
            await client.send_message(chat_id, message)
            print(f"✅ Отправлено в {chat_id}")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"❌ Ошибка в {chat_id}: {str(e)}")
    
    await client.disconnect()
