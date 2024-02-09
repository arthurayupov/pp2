#Example:
#1. 
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#3.
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#4.
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#5.
list1 = ["abc", 34, True, 40, "male"]
#6.
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#7.
thislist = list(("apple", "banana", "cherry")) 
print(thislist)
#8.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#9.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#10.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#11.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#12.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#13.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#14.
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #apple in the list :)
#15.
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #replaced apple with blackcurrant
print(thislist)
#16.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #replaced banana and cherry with blackcurrant and watermelon
print(thislist)
#17.
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #replaced banana with blackcurrant and watermelon
print(thislist)
#18.
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] #replaced banana and cherry with watermelon
print(thislist)
#19.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #added watermelon to third
print(thislist)
#20.
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #added to the end orange
print(thislist)
#21.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #added to the second place orange
print(thislist)
#22.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #added tropical to the end
print(thislist)
#23.
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #added kiwi and orange to the end
print(thislist)
#24.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #removed "banana"
print(thislist)
#25.
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # removed "banana"
print(thislist)
#26.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #showed 2 element
print(thislist)
#27.
thislist = ["apple", "banana", "cherry"]
thislist.pop() #showed the last element
print(thislist)
#28.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#29.
thislist = ["apple", "banana", "cherry"]
del thislist
#30.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Exercise:
#1.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#2.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#3.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#4.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#5.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#6.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#7.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#8.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
