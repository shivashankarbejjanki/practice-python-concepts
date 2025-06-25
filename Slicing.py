#Asccessing parts of a string
string = "shiva shankar"
print(string[0:6])
print(string[3:9])
print(string[:13]) #incase you dont give Starting_index python automatically considers Starting_index as first index
print(string[6:len(string)]) #you can use len(string) as Ending_index
print(string[0:]) #python understoods automatically the last index as Ending_index

#in this Slicing have Starting_index and Ending_index enclosed vth Square Brackets[]
#But Ending_index is not included while printing the output and space is also considered by an index
#Slicing concept is very imp in machine learning

#In python we have Negative indexing @slicing negative index
string1 = "prabhas"
print(string1[-5:-1])
#print(len(string1))