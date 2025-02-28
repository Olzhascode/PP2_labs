# task 1
my_list = [4, 5, 8, 3, 1, 8, 1, 3, 4, 8, 7, 6, 4, 1, 2, 5, 55, 6, 4, 21, 87]
print(sum(my_list))

# task 2
mystring = input("Text something: ")
count_uppercase = 0
count_lowercase = 0
for i in mystring:
    if i.isupper() == True:
        count_uppercase += 1
    elif i.islower() == True:
        count_lowercase += 1
print('number of lowercase letters: ', count_lowercase)
print('number of uppercase letters: ', count_uppercase)

# task 3

text = input("Enter word: ")
m = 0
k = len(text) - 1
flag = True
while m < k:
    if text[m] != text[k]:
        flag = False
        break
    m += 1 
    k -= 1
if flag:
    print("Palindrome")
else:
    print('Not palindrome')

# task 4

import math
import time

def square_root_after_delay(number, delay_ms):

    delay_seconds = delay_ms / 1000.0  
    time.sleep(delay_seconds)  

    square_root = pow(number, 0.5)
    print(f"Square root of {number} after {delay_ms} milliseconds is {square_root}")

number = int(input("Enter number: "))
delay = int(input("Enter milliseconds: "))
square_root_after_delay(number, delay)

# task 5

def is_all_true(tuple):
    return all(tuple)

my_tuple = ()
empty_list = []
flag = True
while flag:
    i = input("Enter element of tuple (enter q to stop): ")
    if i == 'q':
        flag = False
        break
    empty_list.append(i)
my_tuple = tuple(empty_list)
con = is_all_true(my_tuple)
if con:
    print("all elements are True")
else:
    print("not all elements are True")