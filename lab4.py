# Iterators

mytuple = ("apple", "banana", "orange")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print()

mystring = "banana"
myit1 = iter(mystring)

print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print()


#looping Through an iterator

for it in mytuple:
    print(it)
print()

for it in mystring:
    print(it)
print()

# Create an Iterator

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

for it in myiter:
    print(it)
    if it == 5:
        break
