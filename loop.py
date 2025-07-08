"While loop"
"While loop is used for execution of statements untill the given condition is satisfied"

i = 1
while i < 10:
    print(i)
    i += 1;

a = 11
while a <= 15:
    print(a)
    a += 2;



"The break Statement"
"With the break statement we can stop the loop even if the while condition is true:"


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


  "The continue Statement"
"With the continue statement we can stop the current iteration, and continue with the next:"

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)         

  "note in the output 3 is misssing"


  "Python For Loops"
"A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)."

"This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages."

"With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc."


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



  "Looping Through a String"
"Even strings are iterable objects, they contain a sequence of characters:"

for x in "banana":
  print(x)


"The break Statement"
"With the break statement we can stop the loop before it has looped through all the items:"

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


