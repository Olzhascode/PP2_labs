#task 1
def generatorTillN(n):
    for i in range (1, n):
        print(i**2)

n = int(input("Enter number n: "))
generatorTillN(n)
print()


#task 2
def evennums(n2):
    for i in range(n):
        if i % 2 == 0:
            print(i)

n2 = int(input("n2: "))
evennums(n2)
print()


#task 3
def divisibleby(n3):
    for i in range(n3):
        if i % 3 == 0 and i % 4 == 0:
            print(i)

n3 = int(input("n3: "))
divisibleby(n3)
print()


#task 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("a: "))
b = int(input("b: "))
squares_list = list(squares(a, b))
print(squares_list)
print()


#task 5
def reverse(n4):
    for x in range(n4, 0, -1):
        yield x

n4 = int(input('n4: '))
new_list = list(reverse(n4))
print(new_list)