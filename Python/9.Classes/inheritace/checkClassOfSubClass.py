class Base(object):
    pass
class Derived(Base):
    pass

print('Derived is subclass of base: ',issubclass(Derived,Base))
print('Base is subclass of Derived: ',issubclass(Base,Derived))

d=Derived()
b=Base()
print('B is not instance of Derived: ', isinstance(b,Derived))
print('but d is a instance of Base: ',isinstance(d,Base))
