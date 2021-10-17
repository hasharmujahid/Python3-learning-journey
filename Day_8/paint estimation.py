import math
def coverage_estimation():
    height=int(input("enter the height of wall "))
    width=int(input("enter the width of wall "))
    per_can_coverage=5
    calculation=math.ceil((height*width)//per_can_coverage)
    print(f"Total cans required are {calculation} ")
coverage_estimation()