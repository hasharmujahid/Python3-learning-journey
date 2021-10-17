# Write a Python function that checks whether a passed string is palindrome or not.
def palindrome():
    string_input = str(input("enter the string "))
    reversed_string = ''
    for i in range(len(string_input) - 1, -1, -1):
        reversed_string += string_input[i]
    print(reversed_string)
    if reversed_string==string_input:
        print("it is a palindrome")
    else:
        print('it is not a palindrome')


palindrome()
