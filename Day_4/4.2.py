import random
names="hashar ,tayyab ,kinza,nashra"
list_names=names.split(',')
ranint=random.randint(0, len(list_names)-1)

print(list_names[ranint]+' is going to buy meal')

