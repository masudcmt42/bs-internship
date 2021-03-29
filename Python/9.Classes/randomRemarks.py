class Warehouse:
    p='storage'
    r='west'

w1=Warehouse()
print(w1.p,w1.r)
w2=Warehouse()
w2.r='East'
print(w2.p,w2.r)
print(w1.p,w1.r)


#Function Defiend Outside the class
def f1(self,x,y):
    return min(x, x+y)
class C:
    f=f1
    def g(self):
        return 'Hello World'
    h=g

class Bag:
    def __init__(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)


