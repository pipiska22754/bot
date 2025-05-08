import os

def load_list(filename: str) -> list:
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
ADMINS = load_list('admins.txt')
GROUPS = load_list('groups.txt')
