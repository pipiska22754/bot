from telethon import TelegramClient, events
from config import API_ID, API_HASH
from commands import (
    start_handler,
    add_chat_handler,
    stats_handler
)

client = TelegramClient('manager.session', API_ID, API_HASH)

# Регистрация обработчиков
client.add_event_handler(start_handler, events.NewMessage(pattern='/start'))
client.add_event_handler(add_chat_handler, events.NewMessage(pattern='/add_chat'))
client.add_event_handler(stats_handler, events.NewMessage(pattern='/stats'))

client.start()
client.run_until_disconnected()
