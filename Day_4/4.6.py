#Write a Python program that accepts a word from the user and reverse it
name=str(input("enter the word"))
reverse_name=''
for i in range ( len(name)-1,-1,-1):
    reverse_name+=name[i]
print(reverse_name)