class Mother:
    def __init__(self,mName):
        self.mother=mName
    def getMotherName(self):
        return self.mother
class Father:
    def __init__(self,fName):
        self.father=fName
    def getFatherName(self):
        return self.father
class Son(Father,Mother):
    def __init__(self,name,father,mother):
        self.name=name
        Father.__init__(self,father)
        Mother.__init__(self,mother)
    def getName(self):
        return self.name
son=Son('Masud','Yousuf','Shahera')
print(f'Name: {son.getName()}',
        f'Father: {son.getFatherName()}',
        f'Mother: {son.getMotherName()}',sep='\n')

