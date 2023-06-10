# working
import mysql.connector
import datetime
from tabulate import tabulate

db = input("Enter name of your Database: ")

mydb = mysql.connector.connect(host='localhost',user='root',password ='sahaj')
mycursor = mydb.cursor()

sql = "CREATE DATABASE if not exists %s" % (db,)

# if not helps when we create database of same name
# %s will be replaced by db

mycursor.execute(sql)
print("Database created successfully....  ")
mycursor = mydb.cursor()
mycursor.execute("Use " + db)
TableName = input("\nName of the Table to be created : ")

query = "Create table if not exists "+ TableName +"\
(empno int primary key,\
name varchar(15) not null,\
job varchar(15),\
BasicSalary int,\
DA float,\
HRA float,\
GrossSalary float,\
Tax float,\
NetSalary float)"

# table created
print("Table "+ TableName +" Created Successfully....  ")
mycursor.execute(query)

while True:
    print('\n\n\n')
    print("*"*95)
    print('\t\t\t\t MAIN MENU')
    print("*"*95)
    print('\t\t\t 1. Adding Employee Records')
    print('\t\t\t 2. For Displaying Records of all the Employees')
    print('\t\t\t 3. For Displaying Record of a particular Employee')
    print('\t\t\t 4. For Deleting Records of all the Employees')
    print('\t\t\t 5. For Deleting Record of a particular the Employee')
    print('\t\t\t 6. For Modification in a Record')
    print('\t\t\t 7. For displaying Payroll')
    print('\t\t\t 8. For displaying Salary Slips of all Employees')
    print('\t\t\t 9. For displaying Salary Slip of a particular Employee')
    print('\t\t\t 10. To Exit')

    print('Enter Your Choice ----  ',end='')
    choice=int(input())

    if choice==1:
        try:
            print("Enter Employee Information below : ")
            mempno=int(input('Enter Employee Number ---- '))
            mname=input('Enter Employee Name ---- ')
            mjob=input('Enter Employee Job ---- ')
            mbasic=float(input('Enter Basic Salary ---- '))
            if mjob.upper()=='OFFICER':
                mda=mbasic*0.5
                mhra=mbasic*0.35
                mtax=mbasic*0.2
            elif mjob.upper()=='MANAGER':
                mda=mbasic*0.45
                mhra=mbasic*0.30
                mtax=mbasic*0.15
            else:
                mda=mbasic*0.40
                mhra=mbasic*0.25
                mtax=mbasic*0.1
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec=(mempno,mname,mjob,mda,mhra,mgross,mtax,mnet)
            query="insert into " + TableName + " values (%s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(query,rec)
            mydb.commit()
            print("Record added Successfully....  ")

        except Exception as e:
            print('OOPS !!! something when wrong.\nThe Exception occured is --> ',e)


    elif choice==2:
        try:
            query='select * from ' +TableName
            mycursor.execute(query)
            #print(query)
            print(tabulate(mycursor, headers=['EmpNo','Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'], tablefmt='psql'))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
            print(rec)'''

        except Exception as e:
            print('OOPS !!! something when wrong.\nThe Exception occured is --> ',e)

    elif choice==3:
        try:
            en=input("Enter Employee Number of the record to be displayed....  ")
            query="select * from"+TableName+"where empno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\n Record of Employee Number.:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==-1:
                print('Nothing to display')
        except Exception as e:
            print('OOPS !!! something when wrong.\nThe Exception occured is --> ',e)


    elif choice==4:
        try:
            ch=input('Do you want to delete all the records (y/n)')
            if ch.upper()=='Y':
                mycursor.execute('Delete from'+TableName)
                mydb.commit()
                print('All the Records are Deleted....  ')
        except Exception as e:
            print('OOPS !!! something when wrong.\nThe Exception occured is --> ',e)


    elif choice==5:
        try:
            en=input('Enter Employee Number of the Record to be Deleted ---- ')
            query='delete from' + TableName + 'where empno='+en
            mycursor.execute(query)
            mydb.commit()
            c = mycursor.rowcount
            if c>0:
                print("Deletion Done....  ")
            else:
                print('Employee Number',en,'not found')
        except Exception as e:
            print('OOPS !!! something when wrong.\nThe Exception occured is --> ',e)


    elif choice==6:
        try:
            en=input('Enter Employee Number of the Record to be modified ---- ')
            query='select * from'+TableName+'where empno='+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            c=mycursor.rowcount
            if c==-1:
                print('Empno'+en+'does not exist')
            else:
                mname=myrecord[1]
                mjob=myrecord[2]
                mbasic=myrecord[3]
                print('Employee Number : ',myrecord[0])
                print('Name : ',myrecord[1])
                print('Job : ',myrecord[2])
                print('Basic : ',myrecord[3])
                print('DA : ',myrecord[4])
                print('HRA : ',myrecord[5])
                print('Gross : ',myrecord[6])
                print('Tax : ',myrecord[7])
                print('Net : ',myrecord[8])
                print('-----------------------')
                print('Type Value to modify below or just press ENTER for no change')
                x=input('Enter Name ---- ')
                if len(x)>0:
                    mname=x
                x=input('Enter Job ---- ')
                if len(x)>0:
                    mjob=x
                x=input('Enter Basic Salary ----  ')
                if len(x)>0:
                    mbasic=float(x)
                query='update' + TableName + 'ste name=' + "'" + mname + "'" + "'" + 'job' + "'" + ',' + 'basicsalary='\
                       +str(mbasic) + 'where empno=' + en
                print(query)
                mycursor.execute(query)
                mydb.commit()
                print('Record Modified.... ')
        except Exception as e:
            print('OOPS !!! something when wrong.\nThe Exception occured is --> ',e)


    elif choice==7:
        try:
            query='select * from'+TableName
            mycursor.execute(query)
            myrecords=mycursor.fetchall()
            print("\n\n\n")
            print('*'*95)
            print('Employee Payroll'.centre(90))
            print("*"*95)
            now=datetime.datetime.now()
            print("Current Date and Time:",end=' ')
            print(now.steftime("%Y-%m-%d  %H:%M:%S "))
            print()
            print("-"*95)
            print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s'\
                  %('Empno','Name','JobBasic','DA','HRA','Gross','Tax','Net'))
            print('-'*95)
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
            print('-'*95)
        except Exception as e:
            print('OOPS !!! something when wrong.\nThe Exception occured is --> ',e)


    elif choice==8:
        try:
            query='select * from'+TableName
            mycursor.execute(query)
            now=datetime.datetime.now()
            print("\n\n\n")
            print("-"*95)
            print("\t\t\t\t Salary Slip")
            print("-"*95)
            print("Current Date and Time: ",end=' ')
            print(now.strftime("%Y-%m-%d  %H:%M:%S"))
            myrecords=mycursor.fetchall()
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
        except Exception as e:
            print('OOPS !!! something when wrong.\nThe Exception occured is --> ',e)

    elif choice==9:
        try:
            en=input("Enter Employee Number whose PaySlip you want to retrieve ---- ")
            query='select * from '+TableName+' where empno='+en
            mycursor.execute(query)
            now=datetime.datetime.now()
            print("\n\n\n\t\t\t\t Salary Slip")
            print("Current Date and Time: ",end=' ')
            print(now.strftime("%Y-%m-%d  %H:%M:%S"))
            #print(query)
            print(tabulate(mycursor, headers=['EmpNo','Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'], tablefmt='psql'))
        except:
            print("OOPS !!! something when wrong. Try again.... ")

    elif choice==10:
        break

    else:
        print("Please choose a Valid Number")

        

    
