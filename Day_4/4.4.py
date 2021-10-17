numbers=input("enter numbers with sepratos you like")
sepratos=''
for char in numbers:
    if not char.isnumeric():
        sepratos+=char
print(sepratos)
