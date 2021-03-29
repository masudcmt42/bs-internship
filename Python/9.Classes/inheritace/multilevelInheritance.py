class Grandfather:
    def __init__(self,gName):
        self.gName=gName
class Father(Grandfather):
    def __init__(self,gName,fName):
        super().__init__(gName)
        self.fName=fName
class Son(Father):
    def __init__(self,name,fName,gName):
        self.name=name
        super().__init__(gName,fName)
    def printName(self):
        print(f'Grand Father: {self.gName} \nFather Name: {self.fName} \nName: {self.name}\n')

s=Son('Prince','Fakir Chan','Lal Chan')
s.printName()
print(s.gName)
