import numpy as np

# Filtering numpy arrays with boolean Index Lists
'''
np1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(np1)

x = (True,True,True,False,False,False,False,False,False,False)
print(np1[x])
'''
'''
np2 = np.array([1,2,3,4,5,6,7,8,9,10])

filtered = []
for thing in np2:
    if thing % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)

print(np2)
print(filtered)
print(np2[filtered])
'''
# for above one Shortcut i.e is built in function in numpy
np3 = np.array([1,2,3,4,5,6,7,8,9,10])
filtered = np3 % 2 == 0
print(np3)
print(filtered)
print(np3[filtered])


