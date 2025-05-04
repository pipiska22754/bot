from telethon import events
from bot.config import logger

async def start_handler(event):
    try:
        await event.reply(
            "🤖 Бот работает!\n"
            "Доступные команды:\n"
            "/stats - Статистика\n"
            "/logs - Логи (админы)"
        )
    except Exception as e:
        logger.error(f"Start error: {e}")
