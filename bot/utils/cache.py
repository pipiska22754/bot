import time

class StatsCache:
    def __init__(self):
        self.data = []
        self.last_update = 0
        self.cache_ttl = 60  # 1 минута

    async def update(self):
        if time.time() - self.last_update > self.cache_ttl:
            # Заглушка для примера
            self.data = ["user1", "user2"]  
            self.last_update = time.time()
