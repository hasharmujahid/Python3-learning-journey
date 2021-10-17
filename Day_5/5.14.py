l = [1, 2, 3, 4, 5, 6, 87, 2]
l2 = [1, 2, 34, 6, 3, 56, 12]
l3 = []
for i in l:
    for j in l2:
        if not i in l2 and j not in l:
            l3.append(i)
            l3.append(j)

    else:
        pass
print(l3)
