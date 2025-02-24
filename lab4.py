import math

# task 1 

n = int(input('Enter degree: '))
print('radian equal to ', n * (math.pi/180))
print()


# task 2

h = int(input('Enter height: '))
a = int(input('Enter first base: '))
b = int(input('Enter second base: '))
print('Area equal to: ', (a + b)*(h/2))


# task 3
    
s = int(input("Enter number of sides: "))
l = int(input("Enter the length of a polygon: "))
ar = s * (l ** 2) / (4 * math.tan(math.pi / s))
print("Area equal to: ", ar)


# task 4

base = int(input('Enter base: '))
height = int(input('Enter height:'))
print('Area equal to: ', base * height)
