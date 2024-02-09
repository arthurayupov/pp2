#Example:
#1
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#2
myset = {"apple", "banana", "cherry"}
print(type(myset))
#3
set1 = {"abc", 34, True, 40, "male"}
#4
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#5
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#6
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#7
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#8
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#9
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#10
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#11
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#12
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Exercise:
#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
 print("Yes, apple is a fruit!")
#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")