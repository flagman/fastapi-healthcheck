class Base: 
    def __init__(self, optional=False, name="Checker Name"):
        self.optional = optional 
        self.name = name 
    async def check(self):
        raise NotImplementedError