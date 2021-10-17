#
# Write a Python program to check the validity of a password (input from users).
#
# Validation :
#
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
#     Maximum length 16 characters.
import re
password=input('enter your pass word')
x=True
while x:
    if 6>len(password)>16:
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[$#@]",password):
        break
    else:
        print("valid password ",password)
        x=False
        break
