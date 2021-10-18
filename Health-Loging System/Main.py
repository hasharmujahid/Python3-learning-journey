
def tayyab():
    file_selection=input('what you want to log \n 1: Excercise log \n 2: Eating Log :')
    if file_selection=='1':
        file1=open("Tayyab Excercise Log.txt",'a')
        date_time=getdatetime()
        file1.write('[ '+str(date_time)+' ]: ')
        file1.write(input("enter the routine "))
        file1.write('\n')
        file1.close()

    else:
        file1=open("Tayyab Eating Log.txt",'a')
        date_time=getdatetime()
        file1.write('[ '+str(date_time)+' ]: ')
        file1.write(input("enter the routine "))
        file1.write('\n')
        file1.close()


    return file1
def Aanish():
    file_selection=input('what you want to log \n 1: Excercise log \n 2: Eating Log :')
    if file_selection=='1':
        file1=open("Aanish Excercise Log.txt",'a')
        date_time=getdatetime()
        file1.write('[ '+str(date_time)+' ]: ')
        file1.write(input("enter the routine "))
        file1.write('\n')
        file1.close()

    else:
        file1=open("Aanish Eating Log.txt",'a')
        date_time=getdatetime()
        file1.write('[ '+str(date_time)+' ]: ')
        file1.write(input("enter the routine "))
        file1.write('\n')
        file1.close()

    return file1

def Hamza():
    file_selection=input('what you want to log \n 1: Excercise log \n 2: Eating Log :')
    if file_selection=='1':
        file1=open("Hamza Excercise Log.txt",'a')
        date_time=getdatetime()
        file1.write('[ '+str(date_time)+' ]: ')
        file1.write(input("enter the routine "))
        file1.write('\n')
        file1.close()
    else:
        file1=open("Hamza Eating Log.txt",'a')
        date_time=getdatetime()
        file1.write('[ '+str(date_time)+' ]: ')
        file1.write(input("enter the routine "))
        file1.write('\n')
        file1.close()

    return file1

def getdatetime():
    import datetime
    return datetime.datetime.now()
def StartMenu():
    print("""
    ***********                  ***********
  *****************            *****************
*********************        *********************
***********************      ***********************
************************    ************************
*************************  *************************
 **************************************************
  ************************************************
    ********************************************
      ****************************************
         **********************************
           ******************************
              ************************
                ********************
                   **************
                     **********
                       ******
                         **
    """)
    print('welcome to diet Monitoring System Developed by Hashar Mujahid \t\n please select the client \n 1: Tayyab \n 2: Aanish \n 3: Hamza')
    selection=input('enter the number to select the client ')
    if selection=='1':
        tayyab()
    if selection=='2':
        Aanish()
    if selection=='3':
        Hamza()


StartMenu()