import csv
path="E:\GOOGLE AUTOMATION WITH PYTHON\READING CSV\passwords.csv"
with open(path ,'r') as file:
    reading=csv.DictReader(file)

# create a new csv with only useable feilds
    with open("new_csv.csv",'w') as file2:
        filed_names=['type','name','login_uri','login_username','login_password','favorite', 'folder', 'login_totp', 'fields', 'notes', 'reprompt']
        writer=csv.DictWriter(file2 ,fieldnames=filed_names)
        writer.writeheader()
        for line in reading:
            # del line['folder', 'favorite','notes', 'fields', 'reprompt','login_totp']
            writer.writerow(line)
