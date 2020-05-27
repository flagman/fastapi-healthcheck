# FastApi Healthcheck package
```python 
import fastapi_healthcheck
app = FastAPI(...)

class WorkerChecker(healthcheck.base.Base):    
    def check(self):
        status = False 
        # code that checks health
        time_passed_for_check = 1.0
        return {"name": self.name, "status": status, "optional": self.optional, "time": time_passed_for_check}

fastapi_healthcheck.add_health_route(app, name="Super-Resolution", checkers=[
    healthcheck.redis.Checker(),  #built-in checker
    WorkerChecker(name="Worker Checker") #custom checker
])


```
