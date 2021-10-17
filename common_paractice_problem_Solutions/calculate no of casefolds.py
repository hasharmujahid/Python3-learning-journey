# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def case_calculator():
    sample_string = str(input("enter the string "))
    print(len(sample_string))
    upper_case_letters = 0
    lower_case_letters = 0
    for char in sample_string:
        if str.isupper(char) == True:
            upper_case_letters += 1
        else:
            if str.islower(char) == True:
                lower_case_letters += 1
    print('No of uppercase letter is ', upper_case_letters)
    print("no of lower case letter is ", lower_case_letters)


case_calculator()
