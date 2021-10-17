# Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_a_string():
    string_input = str(input("enter the string "))
    reversed_string = ''
    for i in range(len(string_input) - 1, -1, -1):
        reversed_string += string_input[i]
    print(reversed_string)


reverse_a_string()
