# Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_of_all_the_values_in_the_list():
    sum_total = 0
    samplelist = []
    samplelen = int(input("enter the len of the list"))
    for k in range(0, samplelen, 1):
        input_val = input("enter the value ")
        samplelist.append(input_val)
    print(samplelist)

    for i in samplelist:
        sum_total += int(i)
    print(sum_total)


sum_of_all_the_values_in_the_list()
