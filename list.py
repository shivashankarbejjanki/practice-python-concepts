# list is a built-in-data type that stores different types of elements
# list is a mutable

marks = [89.5, 99.2, 80, 75.0, 99.9]
print(marks)
print(marks[2])
print(type(marks)) #you will get type i.e list type
print(len(marks))
print(marks[9]) #gives an error as "list index out of bound"

student = ["shiva", 1201, "Hyderabad"] #you can store different elements in a lists becoz they are mutable(changeble)
print(student)
print(student[1]) #printing index value
student[1] = 8919 #you can change value based on index in lists but not in Strings becoz they are immutable(cannot change)
print(student) 



# LIST() Constructor;
    # By using list() constructor you can create a new list().


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)