your_name=str(input('enter your name'))
target_name=str(input('enter target name'))
combine_string=your_name+target_name
lower=combine_string.lower()
t=lower.count('t')
r=lower.count('r')
u=lower.count('u')
e=lower.count('e')
l=lower.count('l')
o=lower.count('o')
v=lower.count('v')
e=lower.count('e')
calculation=(str(t+r+u+e)+str(l+o+v+e))
if calculation=='10' or calculation ==90:
    print('you go like coke and mentos')
else:
    print('your score was ',calculation,'%')
