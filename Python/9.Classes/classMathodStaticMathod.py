from datetime import date as d
class Person:
    def __init__(self,name,age):
        self.Name=name
        self.age=age
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,d.today().year-year) 
    @staticmethod
    def isAdult(age):
        return age>18
p1=Person('Masud',26)
p2=Person.fromBirthYear('Nafisa',1998)
print(p1.age)
print(p2.age)
print(p1.isAdult(25))
print(type(p2))
