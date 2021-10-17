# line='The quick brown fox jumps over the lazy dog,'
# letters=sorted(line,key=str.casefold)
# print(letters)
# name = ['hashar', 'kinza', 'nashra', 'Hashar', 'Kinza']
# name.sort(key=str.casefold)
# print(name)
LISY=[1,2,32,45,4,55,8,24,23,54,76,45,87,]
LISY.sort()
stop=0
for index,values in enumerate(LISY):
    if values>=10 :
        stop=index
        break

del LISY[:stop]
print(LISY)

start=0
for index in range(len(LISY)-1,-1,-1):
    if LISY[index]<=50:
        start=index+1
        break
del LISY[start:]
print(LISY)