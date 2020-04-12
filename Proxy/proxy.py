from employee import Engineer,Accountant,Admin

class EmployeeProxy(object):
    count = 0

    def __new__(cls, *args):
        instance = object.__new__(cls)
        cls.incr_count()
        return instance
    
    def __init__(self, employee):
        self.employee = employee
    
    @classmethod
    def incr_count(cls):
        cls.count += 1

    @classmethod
    def decr_count(cls):
        cls.count -= 1

    @classmethod
    def get_count(cls):
        return cls.count
    
    def __str__(self):
        return str(self.employee)
    
    def __getattr__(self,name):
        return getattr(self.employee,name)
    
    def __del__(self):
        self.decr_count()

class EmployeeProxyFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        if name == "engineer":
            return EmployeeProxy(Engineer(*args))
        elif name == 'accountant':
            return EmployeeProxy(Accountant(*args))
        elif name == 'admin':
            return EmployeeProxy(Admin(*args))


if __name__=="__main__":
    factory = EmployeeProxyFactory()
    engineer = factory.create('engineer', "sam", 25, "M")
    print(engineer)