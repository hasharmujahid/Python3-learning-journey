# Write a Python program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings. Go to the editor Sample List : ['abc', 'xyz', 'aba',
# '1221'] Expected Result : 2

count = 0
Sample_List= ['abc', 'xyz', 'aba', '1221']
for string in Sample_List:
    if len(string) > 2 and (string[0] == string[-1]):
        count += 1
    else:
        pass
print(count)
