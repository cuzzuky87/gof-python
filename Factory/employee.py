from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return "{} - {}, {} years old {}".format(self.__class__.__name__,
                                                 self.name,
                                                 self.age,
                                                 self.gender)

class Engineer(Employee):
    def get_role(self):
        return "engineeering"

class Accountant(Employee):
    def get_role(self):
        return "accountant"

class Admin(Employee):
    def get_role(self):
        return "administration"

class EmployeeFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        if name == "engineer":
            return Engineer(*args)
        elif name == "accoutnant":
            return Accountant(*args)
        elif name == "admin":
            return Admin(*args)
        else:
            raise ValueError()