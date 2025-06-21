my_list = [1,2,3,4,5]
my_list.append(25)
print(my_list)           # Append means add number to the list at the end.

my_list = [10,20,30,40,50]
my_list.clear()
print(my_list)           # By using clear function empty the list.

my_list = [10,20,30,40,50]
copy_list = my_list.copy()
copy_list.append(100)
my_list.append(1000)

print(my_list, copy_list)     # Copying the same list for multiple times.


my_list = [1,2,3,4,5,6,7,8,9,1,5,8,7,6,6,2,2,4,9,9,9,9]

count = my_list.count(1)
print(count)                    # Count() function is used to count the repeates of a number or string.