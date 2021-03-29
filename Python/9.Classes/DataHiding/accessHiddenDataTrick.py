class Myclass:
    #Hidden Member of MyClass
    __hiddenVariable=0
    def add(self,increment):
        self.__hiddenVariable+=increment
        return self.__hiddenVariable
mm=Myclass()
print(mm.add(100))
print(mm.add(234))
#we can access the value of hidden attribute by a tricky syntex

print(mm._Myclass__heddinVariable)
