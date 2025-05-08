from telethon import events
from config import ADMINS
import os

async def add_chat_handler(event):
    if str(event.sender_id) not in ADMINS:
        return
    
    try:
        chat_id = event.message.text.split()[1]
        with open('groups.txt', 'a') as f:
            f.write(f"{chat_id}\n")
        await event.reply(f"✅ Чат {chat_id} добавлен")
        os.system(f"echo '{chat_id}' >> groups.txt")  # Для GitHub Actions
    except:
        await event.reply("❌ Формат: /add_chat [chat_id]")
