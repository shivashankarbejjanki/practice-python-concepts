# Sets in python are collection of the unordered items
# Each element in the set must be Unique & immutable

# list and Dictionary are cant store in sets bcoz they are mutable(changeble) and sets are immutable(immutable)

Collection = {1, 2, 3, 3, 4, 5, "shiva", "hello", "hello"}
print(Collection) # In sets no Duplicate values are stored
print(type(Collection)) # unordered bcoz values print randomly 
print(len(Collection)) # no duplicate values are counted 


student = {} # Empty Dictionary
print(type(student))

student = set() # this is Empty Set
print(type(student))