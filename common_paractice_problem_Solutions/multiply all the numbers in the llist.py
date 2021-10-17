# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def multiply_of_all_the_values_in_the_list():
    product_total = 1
    samplelist = []
    samplelen = int(input("enter the len of the list"))
    for k in range(0, samplelen, 1):
        input_val = input("enter the value ")
        samplelist.append(input_val)
    print(samplelist)
    for i in samplelist:
        product_total = product_total * int(i)
    print(product_total)
   
multiply_of_all_the_values_in_the_list()
