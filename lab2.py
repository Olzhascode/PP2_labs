# Tuples

# Creating a tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple length
print(len(thistuple))

# Accessing tuple items
print(thistuple[1])  # Accessing the second item (index 1)
print(thistuple[-1]) # Accessing the last item

# Slicing tuples
print(thistuple[1:3])

# Changing tuple values (tuples are immutable, so you need to convert to a list first)
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)

# Looping through a tuple
for x in thistuple:
  print(x)

# Checking if an item exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Joining two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


# Sets

# Creating a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Adding items to a set
thisset.add("orange")
print(thisset)

# Updating a set with multiple items
thisset.update(["mango", "grapes"])
print(thisset)

# Removing an item from a set
thisset.remove("banana") # Raises an error if the item is not present
print(thisset)

thisset.discard("kiwi") # Does NOT raise an error if the item is not present
print(thisset)

# Looping through a set
for x in thisset:
  print(x)

# Checking if an item exists
print("apple" in thisset)

# Joining two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1.update(set2) # adds all items from set2 into set1
print(set1)


# Dictionaries

# Creating a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Accessing dictionary items
print(thisdict["model"])
print(thisdict.get("year"))

# Changing dictionary values
thisdict["year"] = 2018
print(thisdict)

# Adding items to a dictionary
thisdict["color"] = "red"
print(thisdict)

# Removing items from a dictionary
thisdict.pop("model")
print(thisdict)

del thisdict["brand"]
print(thisdict)

# Looping through a dictionary
for x in thisdict: # prints the keys
  print(x)

for x in thisdict.values(): # prints the values
  print(x)

for x, y in thisdict.items(): # prints both keys and values
  print(x, y)

# Checking if a key exists
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary.")


# If else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# while and for loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping through a string
for x in "banana":
  print(x)

# The break statement
for x in fruits:
  print(x)
  if x == "banana":
    break

# The continue statement
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() function
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

i = 1
while i < 6:
  print(i)
  i += 1

# The break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")