# Write a Python function that takes a number as a parameter and check the number is prime or not
def primechecker(number):
    for i in range(2, number, 1):
        if number % i == 0:
            print("its not a prime number")
            break
    else:
        print("it is a prime number")


primechecker(8)