import redis.asyncio as redis

class Cache():
    def __init__(self):
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

    async def set(self, key, value):
        client = redis.Redis(connection_pool=self.pool)
        await client.set(key, value)

    async def get(self, key):
        client = redis.Redis(connection_pool=self.pool)
        value = await client.get(key)
        if not value:
            return None
        return value.decode('utf-8')
