import numpy as np
import sys
import time
SIZE=50
#numPy array Consumed Less Memorry then List
lstX=range(SIZE)
arryX=np.arange(SIZE)
print('size of list: ',sys.getsizeof(6)*len(lstX))
print('Size of numpy array: ',arryX.size*arryX.itemsize)

#NumPy array is fuster then list oprtation

lstY=range(SIZE)
arryY=np.arange(SIZE)

start=time.time()
result=[x+y for x,y in zip(lstX,lstY)]
print((time.time()-start)*1000)
start=time.time()
result2=arryX+arryY
print((time.time()-start)*1000)
#print(result)
#print(result2)

#numpy operatoions
d1=np.array([(2,34,41,4231,41)])
d2=np.array([(2,41,41,65),(23,545,12,54)])
d3=np.array([(32,43,12,53),(323,232,12,32),(23,7,4,2)])
#to know dimention
print(d1.ndim)
print(d3.ndim)
#to know Data type
print(d1.dtype)

#to know byte size each element
print(d1.itemsize)

#to know no of element  of array
print(d1.size)

#to know sshape of element
print(d3.shape)


#re sizing the array
print(d3)
d3=d3.reshape(4,3)
print(d3)

#slicing array

print(d3[1,2]) #the wille print value of row 1 and 3rd col
print(d3[0:,2]) #this will print all element of 3rd col

#line spacing 
a=np.linspace(1,3,5) #genarate 5 value between inclusively[1,3]
print(a)
print(np.linspace(1,3,10)) #generate 10 value [1,3]

a=np.array([32,42,53,12,33,21])
print(a.max())
print(a.min())
print(a.sum())

#find some of axis  0=row, 1=col
a=np.array([(2,32,453,32,65),(32,54,12,75,31)])
print(a.sum(axis=0))
print(a.sum(axis=1))

#Squre root of each elemet
print(np.sqrt(a))
#Standard Deviation
print(np.std(a))

#concatanate two array
b=np.array([(2,32,453,32,65),(32,54,12,75,31)])
print(np.vstack((a,b)))
print(np.hstack((a,b)))
#convart multidimentional to 1D
print(b.ravel())

#Trigonometi
import matplotlib.pyplot as plt
print(np.pi)
x=np.arange(0,3*np.pi,0.1)
y=np.cos(x)
#print(x,y)
plt.plot(x,y)
plt.show()
