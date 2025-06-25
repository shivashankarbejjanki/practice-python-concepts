import numpy as np

# Sort an array Numerical
np1 = np.array([4,2,5,8,9,6,3,1,7,0,])
print(np1)
print(np.sort(np1))

# Alphabetical
np2 = np.array(["shiva","gopal","prudhvi","zoya"])
print(np2)
print(np.sort(np2))

# Booleans T/F
np3 = np.array([True,False,False,True])
print(np3)
print(np.sort(np3))

# Return a copy not change the original
np4 = np.array([4,2,5,8,9,6,3,1,7,0,])
print(np4)
print(np.sort(np4))
print(np4)

# 2-D array
np5 = np.array([[4,7,2,1],[8,3,5,6]])
print(np5)
print(np.sort(np5))