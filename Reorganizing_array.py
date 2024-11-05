import numpy as np

before=np.array([[2,4,1,3],[5,6,8,7]])

print(before)
print (np.shape(before))

after=before.reshape(8,1)
print(after)

after=before.reshape(4,2)
print(after)

after=before.reshape(2,2,2)
print(after)

#after=before.reshape(3,2)   #this reshape dont match with the orginal one
#print(after)

####Vertically Stacking vectors

v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])

print(np.vstack([v1,v2,v2,v2,v2]))

####Horizontally stacking vectors

h1=np.array([1,2,3,4])
h2=np.array([5,6,7,8])

print(np.hstack([h1,h2,h2]))