import aioredis
import time 
import random
import sys
from .base import Base
class Checker(Base):
    def __init__(self, optional=False, url="redis://localhost", name="Redis"):
        super().__init__(optional, name)
        self.redis_url = url
        self.name = name
        self.optional = optional
    async def check(self):
        start = time.time()
        status = False            
        try: 
            redis = await aioredis.create_redis(self.redis_url, encoding='utf-8')                                
            test_key = 'health_check_' + str(random.random()) + str(time.time())
            await redis.set(test_key, 'value')
            result = await redis.get(test_key)
            
            await redis.delete(test_key)            
            status = result == 'value'
            redis.close()
            await redis.wait_closed()
        except:
            print("Warning: ", sys.exc_info()[0])

        time_passed = time.time() - start     
        return {"name": self.name, "status": status, "optional": self.optional, "time": time_passed}

            
        


