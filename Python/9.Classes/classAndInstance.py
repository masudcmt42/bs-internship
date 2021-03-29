class Student:
    versity='DUET'      #Class variable shared by all
    hobbyes=[]  #mistaken use of na class variable
    def __init__(self,name,stid):
            self.name, self.sid =name,stid #instance variable unoque to each objct instance
            self.hobby=[] #create a new empty list for each instance
    def add_hobbyes(self,x):
        self.hobbyes.append(x)
    def add_hobby(self,x):
        self.hobby.append(x)
d=Student('Masud',154103)
e=Student('Nafisa',342334)
print(d.versity)    #shared by all student
print(e.versity)    #shared by all Student
print(d.name,d.sid) #unique to d
print(e.name,e.sid) #unique to e
d.add_hobbyes('cycling') #hobbis for d
e.add_hobbyes('reading') #hobbis for e
print(d.hobbyes) #unexpectedly shared by all

d.add_hobby('gamming')
e.add_hobby('singing')
print(d.hobby)
print(e.hobby)
