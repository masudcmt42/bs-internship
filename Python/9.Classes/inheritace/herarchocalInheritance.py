class Animal:
    def __init__(self):
        self.Leg=4
        self.isTell=True
        self.Lives='Watter'
class Cow(Animal):
    pass
class Fish(Animal):
    pass

c=Cow()
f=Fish()
c.Leg=4
c.isTell=True
c.Lives="Land"
f.Leg=0
f.isTell=False
print("Cow",c.Leg,c.isTell,c.Lives)
print("Fish",f.Leg,f.isTell,f.Lives)

