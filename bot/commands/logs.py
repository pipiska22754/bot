from telethon import events
from bot.config import logger, ADMIN_IDS

async def logs_handler(event):
    try:
        if event.sender_id not in ADMIN_IDS:
            await event.reply("⛔ Доступ запрещен!")
            return
            
        await event.reply(file='bot.log')
    except Exception as e:
        logger.error(f"Logs error: {str(e)}")
