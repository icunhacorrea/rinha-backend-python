import asyncio

from rinhaapi.queue import pessoas_queue

class Worker():
    def __init__(self,
                 queue_timeout=1,
                 queue_batch=100):
        self.queue_timeout = queue_timeout
        self.queue_batch = queue_batch

    async def run(self):
        while True:
            pessoas = []
            while len(pessoas) < self.queue_batch:
                try:
                    pessoa = await asyncio.wait_for(
                        pessoas_queue.get(), timeout=self.queue_timeout
                    )
                    if pessoa:
                        pessoas.append(pessoa)
                except asyncio.TimeoutError:
                    break
                if pessoas:
                    for p in pessoas:
                        print(p)
                

