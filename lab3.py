#Functions


#creating function
def my_function():
  print("Hello from a function")
#calling function
my_function()


#Arguments
def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil") #Emil is an Argument
my_function1("Tobias")
my_function1("Linus")


#Function expects 2 arguments, and gets 2 arguments
def my_function2(fname, lname):
  print(fname + " " + lname)

my_function2("Emil", "Refsnes")


#If the number of arguments is unknown, add a * before the parameter name
def my_function3(*kids):
  print("The youngest child is " + kids[2])

my_function3("Emil", "Tobias", "Linus")


#Keyword Arguments
def my_function4(child3, child2, child1):
  print("The youngest child is " + child3)

my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Arbitrary Keyword Arguments, **kwargs
def my_function5(**kid):
  print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname = "Refsnes")


#Default Parameter Value
def my_function6(country = "Norway"):
  print("I am from " + country)

my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")


#Passing a List as an Argument
def my_function7(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function7(fruits)


#Return Values
def my_function8(x):
  return 5 * x

print(my_function8(3))
print(my_function8(5))
print(my_function8(9))


#The pass Statement
def myfunction9():
  pass


#Positional-Only Arguments
def my_function9(x, /):
  print(x)

my_function9(3)


#Keyword-Only Arguments
def my_function10(*, x):
  print(x)

my_function10(x = 3)


#Combine Positional-Only and Keyword-Only
def my_function11(a, b, /, *, c, d):
  print(a + b + c + d)

my_function11(5, 6, c = 7, d = 8)


#Recursion
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))