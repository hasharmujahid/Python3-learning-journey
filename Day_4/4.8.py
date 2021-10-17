# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
num=''
for i in range(0,6,1):
    if i ==3:
        continue
    else:
        num+=str(i)
print(num)
