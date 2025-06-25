import numpy as np

# copy vs view

np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)

# create a view
#np2 = np1.view()

#print(f'original NP1 {np1}')
#print(f'original NP2 {np2}')

#np1[0] = 1201

#print(f'changed NP1 {np1}')
#print(f'original NP2 {np2}')

# create a copy

np2 = np1.copy()

print(f'original NP1 {np1}')
print(f'original NP2 {np2}')

np1[0] = 1201

print(f'changed NP1 {np1}')
print(f'original NP2 {np2}')