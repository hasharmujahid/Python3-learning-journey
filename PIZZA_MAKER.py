print('welcom to virtual pizza.pk ')
size=input('enter the size of pizza you want S,M,L')
peporoni=input('do you want to add extra peparoni ,Y,N')
cheese=input('do you want to add extra cheese,Y,N')
price=0
if size=='S':
    print('small pizza is selected')
    price+=15
    if peporoni=='Y':
        print('extra tooping added')
        price+=1
    if cheese=='Y':
        print('extra cheese added')
        price+=1
if size=='M':
    print('Medium pizza is selected')
    price+=20
    if peporoni=='Y':
        print('extra peparoni added')
        price+=3
    if cheese=='Y':
        print('extra cheese added')
        price+=1
if size=='L':
    print('small pizza is selected')
    price+=25
    if peporoni=='Y':
        print('extra peparoni added')
        price+=3
    if cheese=='Y':
        print('extra cheese added')
        price+=1
print('total bill was ',price)