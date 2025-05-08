from telethon import events
from config import ADMINS

async def start_handler(event):
    if str(event.sender_id) not in ADMINS:
        return
    
    await event.reply(
        "🤖 **Бот управления рассылкой**\n\n"
        "Доступные команды:\n"
        "/add_chat [id] - Добавить чат\n"
        "/stats - Статистика"
    )
