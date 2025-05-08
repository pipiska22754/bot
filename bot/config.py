import os
from dotenv import load_dotenv

load_dotenv()

def read_list(filename: str) -> list:
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
PHONE = os.getenv('PHONE')
ADMINS = read_list('admins.txt')
GROUPS = read_list('groups.txt')
