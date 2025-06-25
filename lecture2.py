import numpy as np

# slicing numpy arrays
np1 = np.array([1,2,3,4,5,6,7,8,9])
print(np1)

# return 12345
print(np1[1:6])

# return from something till the end of the array i.e 6-9
print(np1[6:])

# Negative slicing i.e backwards
print(np1[-3:-1])

# steps
print(np1[1:5])
print(np1[1:5:2]) # skips 1 digit
print(np1[1:9:3]) # skips 2 digits

# steps on the entire array
print(np1[::2])
print(np1[::3])

# slice a 2d array
np2 = np.array([[1,2,3,4], [5,6,7,8]])
# pull out a single item
print(np2[1,2])