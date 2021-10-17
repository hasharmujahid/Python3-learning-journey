# Write a Python function to check whether a string is a pangram or not. Go to the editor
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
import string
def panagram_checker():
    string_input=str(input("enter the string")).lower()
    alphabets=list(string.ascii_lowercase)
    for char in string_input:
        if char in alphabets:
            print("true")
        else:
            print("false")

panagram_checker()
