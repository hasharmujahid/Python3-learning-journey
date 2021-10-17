import random
options=['rock ','paper','sicssor']
ranint=random.randint(0, len(options)-1)
compmove=options[ranint].lower()
input1=input("enter your move").lower()
if input1==compmove:
    print('draw')
elif (input1=='sicssor' and compmove=='paper') or (input1=='rock' and compmove=='sicssor') or(input1=='paper' and compmove=='rock'):
    print('you won ')
elif (input1=='rock'and compmove=='paper') or (input1=='paper' and compmove=='sicssor') or (input1=='sicssor' and compmove=='rock'):
    print('you lost')
