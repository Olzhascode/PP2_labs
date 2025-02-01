#Classes and Objects

#Create Class
class MyClass:
  x = 5


#Create Object
p1 = MyClass()
print(p1.x)


#__init__
class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person1 = Person1("John", 36)

print(person1.name)
print(person1.age)


#__str__
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person2 = Person2("John", 36)

print(person2)

class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

person3 = Person3("John", 36)

print(person3)


#Object Methods
class newPerson:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunction(self):
    print("Hello my name is " + self.name)

newperson = newPerson("John", 36)
newperson.myfunction()


