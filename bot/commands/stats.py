from telethon import events
from bot.utils.cache import StatsCache
from bot.config import logger

async def stats_handler(event):
    try:
        cache = StatsCache()
        await cache.update()
        await event.reply(f"📊 Всего пользователей: {len(cache.data)}")
    except Exception as e:
        await event.reply("❌ Ошибка статистики")
        logger.error(f"Stats error: {str(e)}")
