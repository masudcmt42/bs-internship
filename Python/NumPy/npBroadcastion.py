import numpy as np
# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y=np.empty_like(x) #crate empty vector like dimention of x

#add vector v in each row
row,col=x.shape
for i in range(row):
    y[i,:]=x[i,:]+v
print(y)

#another way
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv=np.tile(v,(4,1))

y=x+vv
print(y)

#efficient Way

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
print(x+v)
