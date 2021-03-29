class Base:
    def __init__(self,x):
        self.x=x
class Derived(Base):
    def __init__(self,x,y):
        self.y=y
        Base.x=x
    def printXY(self):
        print(Base.x,self.y)

if __name__=="__main__":
    import sys
    d=Derived(sys.argv[1],sys.argv[2])
    d.printXY()

