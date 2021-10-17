def factorial():
    number_to_find_factorial=int(input("enter a number"))
    factorial=1
    if number_to_find_factorial>=0:
        for i in range(1,number_to_find_factorial+1,1):
            factorial=factorial*i
        print(factorial)
    else:
        print("invalid value \n\t make sure value is greater than 0")
factorial()