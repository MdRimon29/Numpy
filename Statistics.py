import numpy as np

a=np.array([[2,5,3],[4,1,6]])

print(a)
print (np.min(a,axis=1))

print(np.max(a,axis=0))

print(np.sum(a,axis=1))
