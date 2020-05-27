from .checkers import redis
from .checkers import base
def add_health_route(app, name="Application Name", checkers=[], version=1.0):        
    async def health_route():
        checks = [] 
        for checker in checkers: 
            checks.append(await checker.check())

        status = True                 
        for check in checks: 
            if not check['optional'] and check['status'] is False:
                status = False 
        return {"name": name, "status": status, "version": version, "checks": checks}

    app.get('/health')(health_route)