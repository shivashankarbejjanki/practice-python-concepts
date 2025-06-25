my_list = [1,2,3,4,5]
my_list.append(25)
print(my_list)           # Append means add number to the list at the end.

my_list = [10,20,30,40,50]
my_list.clear()
print(my_list)           # By using clear function empty the list.

my_list = [10,20,30,40,50]
copy_list = my_list.copy()
copy_list.append(100)           # Adding new elements to the copied list
my_list.append(1000)

print(my_list, copy_list)     # Copying the same list for multiple times.


my_list = [1,2,3,4,5,6,7,8,9,1,5,8,7,6,6,2,2,4,9,9,9,9]

count = my_list.count(1)
print(count)                    # Count() function is used to count the repeates of a number or string.



my_list = [1,2,3,4,5]
my_list.extend([6,7,8,9])

print(my_list)                  # Extend() function used for extending the line.




my_list = [1,2,4,5]
my_list.insert(2,3)

print(my_list)                      # insert() function is used for add element in middle wherever you want.



my_list = [1,2,3,4,5]
my_list.remove(4)

print(my_list)              # By using remove() function we can able to remove directly the value you want to remove.

my_list.pop()               # here POP() function removes directly the last one.
print(my_list)

my_list.pop(1)              # here POP() function removes based on given index.
print(my_list)



my_list = [1,2,3,4,5]

my_list.reverse()
print(my_list)              # By using reverse() function you can reverse the list.



my_list = [5,4,8,3,9,7,6]

my_list.sort()              # By using SORT() function you can arrange the elements into ascending order.
my_list.sort(reverse=True)      # here By using SORT() function you can arrange in Descending order
print(my_list)



String_list = ["shiva", "akshaya", "priya", "lakshmi"]
String_list.sort()
print(String_list)              # here by using SORT() function you can arrange the string_list in alphabatic order.

