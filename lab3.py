#Inheritance

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


#Add the __init__() Function

class KBTU_Student(Person):
   def __init__(self, fname, lname):
     self.firstname = fname
     self.lastname = lname
  
   def printStudent_name(self):
     print(self.firstname, self.lastname)

#Use the super() Function
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

y = Student('Jake', 'Brown', 2028)

#Add Methods

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Jake", "Brown", 2028)
x.welcome()
