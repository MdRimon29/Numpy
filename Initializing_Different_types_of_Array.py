import numpy as np

#all zeros matrix
#print (np.zeros((2,3)))

#all ones matrix
#print (np.ones((4,2,3),dtype='int32'))

#any other numbers
#print( np.full((2,2),90,dtype='float32'))

#a = np.array([[1,2,3,4,5],[3,4,5,6,7]],dtype='int16')
#print(np.full_like(a,99))
#print(np.full(a.shape,99))

#import any random number
#print(np.random.rand(4,2,3))

#random integer values
#print(np.random.randint(2,7, size=(3,4)))  #select random number,but start form 2 and till 6(before 7).row size 3,comlumn size 4


#the identity matrix
#print(np.identity(5))

#repeat an arrray
#arr=np.array([[4,2,3],[1,2,3]])
#r1=np.repeat(arr,3,axis=1)
#print(r1)

#make a matrix
#arr=np.ones((5,5),dtype='int32')
#a=np.zeros((3,3),dtype='int32')
#a[1,1]=9
#arr[1:-1,1:-1]=a
#print (arr)

#make a copy
a=np.array([1,2,3])
b=a.copy()      #if we dont use copy then change of b also occur change of a
b[0]=100

print (a)


##we can index with a list in numpy
b=np.array([1,2,3,4,5,6,7,8,9])
print(b[[2,4,6]])