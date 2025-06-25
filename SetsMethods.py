# Set.add() --> Adds an element

student = {"shiva", "apple", 1201, 8919653116, "world", "welcome", "world", 1201}
print(student)
print(len(student))

student.add("mathew")
print(student)

# set.remove() --> Remove the elements in the set

student.remove(8919653116)
print(student)

# set.pop() --> eliminates the elements randomly you want to eliminate

student.pop()
print(student)
print(student)

# set.clear() --> empties the set

student.clear()
print(student)
print(len(student))

#set.union(set2) --> combines both set values & returns new by removing Duplicates

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

#set.intersection(set2) --> combines common values and returns new (returns common values )

print(set1.intersection(set2))


