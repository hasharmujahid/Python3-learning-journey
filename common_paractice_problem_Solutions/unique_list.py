# Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
# to myself i can also put list as a perameter but i wnted to practce to get inputs okay dont judgeeeee meeeeeee or judge me idc

def unique_list():
    samplelist = []
    unique_list = []
    samplelen = int(input("enter the len of the list"))
    for k in range(0, samplelen, 1):
        input_val = input("enter the value ")
        samplelist.append(input_val)
    print(samplelist)
    for i in samplelist:
        if i not in unique_list:
            unique_list.append(i)
    print("your unique list is", unique_list)
unique_list()
