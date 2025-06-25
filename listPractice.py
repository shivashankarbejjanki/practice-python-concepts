# practice problems

movies = []
movies.append(input("enter the name of First movie: "))
movies.append(input("enter the name of second movie: "))
movies.append(input("enter the name of third movie: "))
print(movies)


list1 = [1, 2, 1]

copy_list1 = list1.copy
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")