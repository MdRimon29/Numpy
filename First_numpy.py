import numpy as np

a = np.array([[1,2,3,4,5],[3,4,5,6,7]],dtype='int16')
b=np.array([2.0,3.5,5.1])

#two dimentiion array
print(a)

#get dimension
print(a.ndim)

#get shape
print(a.shape) #row,column

#get type
print(a.dtype)

#get size
print(a.itemsize)

#number of elements
print(a.size)

#number of totalsize(in bytes)
print(a.nbytes)     #totalsize=(itemsize*size)

print(b.dtype)