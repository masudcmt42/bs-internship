import numpy as np

a=np.array([12,12,43,12,32])
print(type(a))
print(a.shape)
for x in range(a.size):
    print(a[x])

a[1]=20
print(a)

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

