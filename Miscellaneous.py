import numpy as np

a=np.genfromtxt('data3.txt',delimiter=',',dtype='int32')
print (a)

###Boolean masking and advance indexing
print(a>50)
print (a[a>50])
print(np.all(a>50,axis=1))  #all value in a axis is greater than 50
print(((a>50)&(a<100)))
print(~((a>50)&(a<100)))
