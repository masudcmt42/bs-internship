class Person:
    def __init__(self,fname,lname):
        self.fName,self.lName=fname,lname
    def getName(self):
        return self.fName+' '+self.lName
    def isEmployee(self):
        return False
class Employee(Person):
    def isEmployee(self):
        return True
emp=Person('Nafisa','Anjum')
print(emp.getName(),' is ', 'Employee' if emp.isEmployee() else 'Not Employee')
emp1=Employee('Sojib','pal')
print(emp1.getName(),' is ', 'Employee' if emp1.isEmployee() else 'Not Employee')
