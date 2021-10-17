# Write a Python program to find the list of words that are longer than n from a given list of words.

lw=['hashar','kinza','nashra',"tayyab","The", "quick", 'over', "the" ,"lazy" ,"dog"]
n= int(input('what is the lenght of the word you want to seprate'))
for i in lw:
    if len(i)>n:
        print(i)
    else:pass

