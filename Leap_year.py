year=int(input('enter the year: '))
if year%4==0 and year%100==0 and year%400==0:
    print(f'{year}is the leap year containg 366 days ')
else:
    print('not a leap year')