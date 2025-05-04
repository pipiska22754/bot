import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Настройки Telegram
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
ADMIN_IDS = set(map(int, os.getenv('ADMIN_IDS').split(',')))
BOT_SESSION = 'bot_session'

# Логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
