list=['hashar','kinza',"tayyab",'nashra',"samina",'mujahid']
found=input("enter the name on person you want to get").lower()
found_at=None
for i in range(len(list)):
    if list[i]==found:
        found_at=i
        break

print("item found at {0}".format(found_at))