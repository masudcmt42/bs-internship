class Bird:
    def intro(self):
        return 'there are many types of bired'
    def flight(self):
        return 'most of birds can fly but sime cant'
class Sparrow(Bird):
    def flight(self):
        return 'Sparrow can fly.'
class Ostrich(Bird):
    def flight(self):
        return 'Ostrich can\'t fly.'
bird=Bird()
sp=Sparrow()
os=Ostrich()
print(bird.intro())
print(bird.flight())

print(sp.intro())
print(sp.flight())

print(os.intro())
print(os.flight())




