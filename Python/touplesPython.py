#Create a Tuple 
dimensions=(1213,4523,5683,5652,8963,9062)
print(dimensions)

#Create tuple using comma 
t=1234,4342,'Hello'
print(t)

#tuple may be nested
u=t,(1,2,3,4,5),dimensions
print(u)
print(t[1])


'''python List and Tuples are all most same
    but main difference between python list and tuples is onece 
    touples is created then it never be change. we can't modified it
'''

#Revarce Touple
print(dimensions[::-1])

#tuple contain mutable object
v=([2,4,6,8],[1,3,5,7,9])
print(v)

#create tuple one or empty items
empty=()
single='One', #<--- note the trailing comma
print(len(empty))
print(len(single))
'''The statement t = 12345,54321,'hello!'is an example of tuple packing:
   the values 12345,54321 and 'hello!' are packed together in a tuple.
   The reverse operation is also possible:'''
x, y, z = t
print(x,y,z)

'''This is called, appropriately enough, sequence unpacking and works 
   for any sequence on the right-hand side.'''





