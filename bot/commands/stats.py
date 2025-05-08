from telethon import events
import os

async def stats_handler(event):
    try:
        with open('groups.txt', 'r') as f:
            count = len(f.readlines())
        await event.reply(f"📊 Чатов в рассылке: {count}")
    except:
        await event.reply("❌ Файл groups.txt не найден")
