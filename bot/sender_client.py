from telethon import TelegramClient
from telethon.sessions import StringSession
from config import API_ID, API_HASH, PHONE
import asyncio

async def main():
    # Чтение сообщения из файла
    with open('message.txt', 'r') as f:
        message = f.read().strip()

    # Чтение списка чатов
    with open('groups.txt', 'r') as f:
        groups = [line.strip() for line in f if line.strip()]

    # Авторизация
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        code = input("Введите код из Telegram: ")
        await client.sign_in(PHONE, code)

    # Рассылка
    for chat_id in groups:
        try:
            await client.send_message(int(chat_id), message)
            print(f"✅ Отправлено в {chat_id}")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"❌ Ошибка в {chat_id}: {str(e)}")

    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())