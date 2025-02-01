#OPERATORS
print(10+5) # 15

print(100 + 5 * 3) # '*' has higher precedence than addition '+' 

print(5 + 4 - 7 + 3) # + and - have the same precedence
print()




#LIST

#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

#using type() 
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class, list>

#Using the list() constructor to make a List:
mylist = list(("apple", "banana", "cherry"))
print(mylist)

#Access Items

mylist = ["apple", "banana", "cherry"]
print(mylist[1])

# using negative indexing
mylist = ["apple", "banana", "cherry"]
print(mylist[-1])

#returns [3;4;5] iteams
newlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(newlist[2:5]) 

print(newlist[:4]) #returns iteans form beginning to 'kiwi' 

print(newlist[2:]) #returns iteans form "cherry" to the end

print(newlist[-4:-1]) #returns the items from "orange" (-4) to, but NOT including "mango" (-1)

if "apple" in newlist:
  print("Yes, 'apple' is in the fruits list")

#Change iteam vlaue
list4 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list5 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list6 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

list4[1] = "orange"
print(list4)

list5[1:3] = ["orange", "watermelon"]
print(list5)

#Change the second value by replacing it with two new values
list6[1:2] = ["orange", "watermelon"]
print(list6)

# using insert
list7 = ["apple", "banana", "cherry"]
list7.insert(2, "watermelon")
print(list7)

#Add List Items

#appaend()
list8 = ["apple", "banana", "cherry"]
list8.append("ornage")
print(list8)

#insert()
list9 = ["apple", "banana", "cherry"]
list9.insert(1, "orange")
print(list9)

#Add the elements of tropical to thislist
list10 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
list10.extend(tropical)
print(list10)

#Add elements of a tuple to a list:
list11 = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")
list11.extend(tuple)
print(list11)

#Remove List Items

#Remove "banana"
list12 = ["apple", "banana", "cherry"]
list12.remove("banana")
print(list12)

#Remove the first occurrence of "banana"
list13 = ["apple", "banana", "cherry", "banana", "kiwi"]
list13.remove('banana')
print(list13)

#Remove the second item, method pop()
list14 = ["apple", "banana", "cherry", "banana", "kiwi"]
list14.pop(1)
print(list14)

#Remove the first item, method del
list15 = ["apple", "banana", "cherry", "banana", "kiwi"]
del list15[0]
print(list15)

#Delete the entire list
list16 = ["apple", "banana", "cherry"]
del list16

#Clear the list
list17 = ["apple", "banana", "cherry"]
list17.clear()
print(list17)

#Loop Lists
list18 = ["apple", "banana", "cherry"]
for i in list18:
  print(i)

#Print all items by referring to their index number
for i in range(len(list18)):
  print(list18)

#Print all items, using a while loop
while i < len(thislist):
  print(list18[i])
  i = i + 1

#a short hand for loop that will print all items in a list
[print(i) for i in list18]


# List Comprehension

list_fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [x for x in list_fruits if "a" in x]
print(new_list)

new_list2 = [x for x in list_fruits if x != "apple"]
print(new_list2)
new_list3 = [x for x in list_fruits]
print(new_list3)
new_list4 = [x for x in range(10)]
print(new_list4)

new_list5 = [x for x in range(10) if x < 5]
print(new_list5)

new_list6 = [x.upper() for x in list_fruits]

new_list7 = ['hello' for x in list_fruits]

new_list8 = [x if x != "banana" else "orange" for x in list_fruits]

fruits_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits_list.sort()
print(fruits_list)

#decreasing sort
fruits_list.sort(reverse = True)
print(fruits_list)

fruits_list.reverse()
print(fruits_list)

#Copy list
list19 = ["apple", "banana", "cherry"]
my_list = list19.copy()
print(my_list)

list20 = ["apple", "banana", "cherry"]
my_list1 = list(thislist)
print(my_list1)

# Join Two Lists
list21 = ["a", "b", "c"]
list22 = [1, 2, 3]

list23 = list21 + list22
print(list23)

# Append list2 into list1:
list31 = ["a", "b" , "c"]
list32 = [1, 2, 3]

for x in list32:
  list31.append(x)

print(list31)


# list methods

"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""