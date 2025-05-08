from telethon import TelegramClient, events
from config import API_ID, API_HASH, ADMINS

client = TelegramClient('manager.session', API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/add_chat'))
async def add_chat(event):
    if str(event.sender_id) not in ADMINS:
        return
    
    chat_id = event.message.text.split()[1]
    with open('groups.txt', 'a') as f:
        f.write(f"{chat_id}\n")
    await event.reply(f"✅ Чат {chat_id} добавлен")

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("Бот управления рассылкой готов к работе!")

client.start()
client.run_until_disconnected()
