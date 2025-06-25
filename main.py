import numpy as np 

np1 = np.array([1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

#range
np2 = np.arange(9)
print(np2)

#step
np3 = np.arange(1,9,2)
print(np3)

#zeros
np4 = np.zeros(9)
print(np4)

#multi dimensional zeros
np5 = np.zeros((2,9))
print(np5)

#full
np6 = np.full((10),5)
print(np6)

#multi dimensional full
np7 = np.full((2,10),5)
print(np7)

#convert lists into numpy
list1 = [1,2,3,4,5,6,7,8,9]
print(list1)
np8 = np.array(list1)
print(np8)
print(np8[0])
print(np8[5])