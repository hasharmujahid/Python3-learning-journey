numebr = int(input("enter the number "))
boolean_value = bool(input("enter true or false "))
if boolean_value is True:
    for i in range(0, numebr + 1, 1):
        print('*' * i)
else:
    for i in range(numebr, -1, -1):
        print('*' * i)
