import os
dir=str(input("enter the path of the directory: "))
for name in os.listdir(dir):
    full_name=os.path.join(dir,name)
    if os.path.isdir(full_name):
        print('{} is a directory'.format(full_name))
    else:
        print('{} is a file'.format(full_name))
