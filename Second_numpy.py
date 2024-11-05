import numpy as np

a=np.array([[1,2,3,4,5,6,7],[3,4,5,6,7,8,9]])

#get a specific element
#print(a[1,2])

#get a specific row
#print(a[1,:])

#get a specific column
#print(a[:,0])

#getting more fancy
#print(a[0, 1:-1:2])      #a[startindex:endindex:stepsize]

#a[1,5]=20
#print (a)

#a[:,3]=40
#print (a)

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
#print(b[0,1,0])
#print(b[:,1,:])

b[:,1,:]=[[9,9],[8,8]]

print (b)
print(b.shape)