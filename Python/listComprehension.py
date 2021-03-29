sq=list(map(lambda x:x**2, range(10)))
print(sq)

sq.clear()

sq=[x**3 for x in range(0,20,2)] # in range(start,stop,step)
print(sq)

#Complex 

print([(x, y) for x in [2,3,4] for y in [3,4,5] if x!=y])

vec=[-4,-2,0,2,4]
#create a new list using vec value double
print('double of value vec ',[x*2 for x in vec])
#filter the list excluding nageative
print('filter list excluding nage ',[x for x in vec if x>=0])
print('apply abs() function ',[abs(x) for x in vec])
#Craeate 2-tuple list (numbwer,squre)
print([(x,x**2) for x in range(6)])
# flatten a list using a listcomp with two for
vec=[[1,2,3],[4,5,6],[7,8,9]]
print([item for sublist in vec for item in sublist])

from math import pi
print([str(round(pi,i))for i in range(1,6)])
