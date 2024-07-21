import random
import string

char_upper = string.ascii_uppercase
char_lower = string.ascii_lowercase
digits = string.digits
char_special = string.punctuation

list = []

# Choose password length
length = int(input("Password length: "))

# Criteria
q1 = input("Uppercase: ")
if q1 in ['y', "yes"]:
    list.append(char_upper)
    
q2 = input("Lowercase: ")
if q2 in ['y', "yes"]:
    list.append(char_lower)

q3 = input("Numbers: ")
if q3 in ['y', "yes"]:
    list.append(digits)

q4 = input("Special characters: ")
if q4 in ['y', "yes"]:
    list.append(char_special)

# Generate password
for _ in range(length):
    i = random.choice(list)
    j = random.choice(i)
    print(j, end="")