print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

a = 200
b = 33

if b < a:
    print("b is greater than a")
else:
    print("b is not greater than a") 

print(bool("Hello"))
print(bool(15))

bool("abc") # any string, numbers, dictionary except empty ones will be true
bool("123")
bool(['apple', 'cherry', 'banana'])

bool("") #Fasle
bool(0) #Fasle

# Print Yes if function returns True or No if function returns False
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#check if an object is an int or not
x = 200
print(isinstance(x, int))

