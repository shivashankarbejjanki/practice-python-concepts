string = "i am learning from python programming language from apnaCollege"
print(string)

#endswith()----
print(string.endswith("ege"))

#capitalize()----
print(string.capitalize())

#replace(old,new)----
print(string.replace("learning", "studying"))
print(string.replace("o","a"))

#find()----
print(string.find("p")) 
print(string.find("learning")) #shows index of first letter when you enter word
print(string.find("z")) #prints negative value note: negative values only valid for slicing only 

#count()----
print(string.count("python"))
print(string.count("p"))
print(string.count("from"))

#practice programs
name = input("Enter the name: ")
print(name)
print(len(name))

string = "My name i$ $hiva $hankar"
print(string.count("$"))