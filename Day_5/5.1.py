heights=[123,125,136,157,176,152,156,187,136,198]
sum=0
count=0
for i in heights:
    sum+=i
    count+=1
avg=sum/count
print(sum)
print(count)
print('average height of student is ',avg)
