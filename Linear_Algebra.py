import numpy as np

a=np.ones((2,3),dtype='int32')
b=np.full((3,2),2,dtype='int32')

print (a)
print (b)
print(np.matmul(a,b))

#determinant of a matrix
c=np.identity(3)

print(np.linalg.det(c))