def primenumber_checker(number):
    for i in range(2,number):
        if number%i==0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
primenumber_checker(938)