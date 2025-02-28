import re

# Task 1
def match_ab_zero_or_more():
    pattern = r"ab*"
    print("TASK 1")
    test_strings = input("Enter strings separated by space: ").split()
    for s in test_strings:
        if re.fullmatch(pattern, s):
            print(f"'{s}' matches the pattern.")
        else:
            print(f"'{s}' does not match the pattern.")
match_ab_zero_or_more()

# Task 2
def match_ab_two_to_three():
    pattern = r"ab{2,3}"
    print("TASK 2")
    test_strings = input("Enter strings separated by space: ").split()
    for s in test_strings:
        if re.fullmatch(pattern, s):
            print(f"'{s}' matches the pattern.")
        else:
            print(f"'{s}' does not match the pattern.")
match_ab_two_to_three()

# Task 3
def find_lowercase_underscore():
    pattern = r"[a-z]+_[a-z]+"
    print("TASK 3")
    test_strings = input("Enter strings separated by space: ").split()
    for s in test_strings:
        if re.search(pattern, s):
            print(f"'{s}' contains a match.")
        else:
            print(f"'{s}' does not contain a match.")
find_lowercase_underscore()

# Task 4
def find_uppercase_lowercase():
    pattern = r"[A-Z][a-z]+"
    print("TASK 4")
    test_strings = input("Enter strings separated by space: ").split()
    for s in test_strings:
        if re.search(pattern, s):
            print(f"'{s}' contains a match.")
        else:
            print(f"'{s}' does not contain a match.")
find_uppercase_lowercase()

# Task 5
def match_a_anything_b():
    pattern = r"a.*b$"
    print("TASK 5")
    test_strings = input("Enter strings separated by space: ").split()
    for s in test_strings:
        if re.search(pattern, s):
            print(f"'{s}' contains a match.")
        else:
            print(f"'{s}' does not contain a match.")
match_a_anything_b()

# Task 6
def replace_space_comma_dot_colon():
    print("TASK 6")
    text = input("Enter a sentence: ")
    pattern = r"[ ,.]"
    print(re.sub(pattern, ":", text))
replace_space_comma_dot_colon()

# Task 7
def snake_to_camel():
    print("TASK 7")
    snake_str = input("Enter a snake_case string: ")
    components = snake_str.split('_')
    print(components[0] + ''.join(x.title() for x in components[1:]))
snake_to_camel()

# Task 8
def split_at_uppercase():
    print("TASK 8")
    text = input("Enter a camelCase string: ")
    print(re.split(r'(?=[A-Z])', text))
split_at_uppercase()

# Task 9
def insert_spaces_before_uppercase():
    print("TASK 9")
    text = input("Enter a camelCase string: ")
    print(re.sub(r"([A-Z])", r" \1", text).strip())
insert_spaces_before_uppercase()

# Task 10
def camel_to_snake():
    print("TASK 10")
    camel_str = input("Enter a camelCase string: ")
    print(re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower())
camel_to_snake()
