import asyncio
from telethon import TelegramClient
from bot.config import API_ID, API_HASH, BOT_SESSION
from bot.commands import register_handlers

class TelegramBot:
    def __init__(self):
        self.client = TelegramClient(BOT_SESSION, API_ID, API_HASH)
    
    async def run(self):
        await self.client.start()
        print("Бот запущен!")
        register_handlers(self.client)
        await self.client.run_until_disconnected()

if __name__ == '__main__':
    bot = TelegramBot()
    asyncio.run(bot.run())
