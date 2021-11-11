import csv
path="E:\GOOGLE AUTOMATION WITH PYTHON\READING CSV\passwords.csv"
with open(path ,'r') as file:
    reading=csv.reader(file)
    # or dictreader is also a good option
    for line in reading:
        # unpack values
        print(line)
        # a,b,type_of_account,name,n,f,reprompt,login_url,login_username,login_password,l=line
        # print(f'type of account is : {type_of_account} \nwebsite where account is : {name} \nlink_to the website :{login_url} \nlogin username is : {login_username}, \npassword is :{login_password}\n\n\n')