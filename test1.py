# working
import mysql.connector
import datetime
from tabulate import tabulate

db = input("Enter name of your Database: ")

mydb = mysql.connector.connect(host='localhost',user='root',password ='sahaj')
mycursor = mydb.cursor()

''' this function checks if database exists or not
returns 1 if database exists
returns 0 if database does not exists '''

def check_database_exists(host, username, password, db):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=db
        )
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")

        result = cursor.fetchone()
        if result[0] == db:
            print(f"The database '{db}' exists.")
            return 1
        else:
            print(f"The database '{db}' does not exist.")
            return 0
    
    except mysql.connector.Error as error:
        print(f"The database '{db}' does not exist.")
        return 0

exist = check_database_exists('localhost', 'root', 'sahaj', db)

if exist == 0:
    sql = "CREATE DATABASE " + db
    mycursor.execute(sql)
    print("Successfully created Database " + db)
    mycursor = mydb.cursor()
    mycursor.execute("Use " + db)
else:
    mycursor.execute("Use " + db)
    print("Opening ......")

table_name = input("\nEnter Table Name: ")

''' this function checks if table exists in a database or not
returns 1 if table exists
returns 0 if table does not exists '''

def check_table_exists(host, username, password, database_name, table_name):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database_name
        )
        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")

        result = cursor.fetchone()
        if result:
            print(f"The table '{table_name}' exists in the database '{db}'.")
            return 1
        else:
            print(f"The table '{table_name}' does not exist in the database '{db}'.")
            return 0
    
    except mysql.connector.Error as error:
        print(f"The table '{table_name}' does not exist in the database '{db}'.")
        return 0

table_check = check_table_exists('localhost', 'root', 'sahaj', db, table_name)

if table_check == 0:
    query = "CREATE TABLE " + table_name + "\
    (empno int primary key,\
    name varchar(15) not null,\
    job varchar(15),\
    BasicSalary int,\
    DA float,\
    HRA float,\
    GrossSalary float,\
    Tax float,\
    NetSalary float)"

    mycursor.execute(query)
    print("Table "+ table_name +" Created Successfully....  ")
else:
    print("Operations will be performed in the Table ",table_name)
    

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
    print("Enter the number from the options")

    print('Enter Your Choice ----  ',end='')
    choice = (input())

    if choice == '1':
        try:
            print("Enter Employee Information below : ")
            mempno = int(input('Enter Employee Number ---- '))
            mname = input('Enter Employee Name ---- ')
            mjob = input('Enter Employee Job ---- ')
            mbasic = float(input('Enter Basic Salary ---- '))

            if mjob.lower() == 'officer':
                mda = mbasic * 0.5
                mhra = mbasic * 0.35
                mtax = mbasic * 0.2

            elif mjob.lower() == 'manager':
                mda = mbasic * 0.45
                mhra = mbasic * 0.30
                mtax = mbasic * 0.15

            else:
                mda = mbasic * 0.40
                mhra = mbasic * 0.25
                mtax = mbasic * 0.1

            mgross = mbasic + mda + mhra
            mnet = mgross - mtax
            rec = (str(mempno), mname, mjob, str(mbasic), str(mda), str(mhra), str(mgross), str(mtax), str(mnet))

            query = "INSERT INTO " + table_name + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            mycursor.execute(query,rec)
            mydb.commit()
            print("Record added Successfully....  ")

        except Exception as e:
            print('OOPS !!! something went wrong.\nThe Exception occured is --> ', e)


    elif choice == '2':
        try:
            query = 'select * from ' + table_name
            mycursor.execute(query)
            print(tabulate(mycursor, headers=['EmpNo','Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'], tablefmt='psql'))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
            print(rec)'''

        except Exception as e:
            print('OOPS !!! something went wrong.\nThe Exception occured is --> ',e)

    elif choice == '3':
        try:
            en=input("Enter Employee Number of the record to be displayed....  ")
            query="select * from"+ table_name +"where empno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\n Record of Employee Number.:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==-1:
                print('Nothing to display')
        except Exception as e:
            print('OOPS !!! something went wrong.\nThe Exception occured is --> ',e)


    elif choice == '4':
        try:
            ch=input('Do you want to delete all the records (y/n) --- ')
            if ch.lower()=='y':
                mycursor.execute('DROP TABLE '+ table_name)
                mydb.commit()
                print('All the Records are Deleted....  ')
                table_name = input("\nEnter Table Name: ")
                table_check = check_table_exists('localhost', 'root', 'sahaj', db, table_name)

                if table_check == 0:
                    query = "CREATE TABLE " + table_name + "\
                    (empno int primary key,\
                    name varchar(15) not null,\
                    job varchar(15),\
                    BasicSalary int,\
                    DA float,\
                    HRA float,\
                    GrossSalary float,\
                    Tax float,\
                    NetSalary float)"

                    mycursor.execute(query)
                    print("Table "+ table_name +" Created Successfully....  ")
                else:
                    print("Operations will be performed in the Table ",table_name)


            else:
                continue
        except Exception as e:
            print('OOPS !!! something went wrong.\nThe Exception occured is --> ', e)


    elif choice == '5':
        try:
            en = input('Enter Employee Number of the Record to be Deleted ---- ')
            query = 'DELETE FROM ' + table_name + ' WHERE empno='+ en
            mycursor.execute(query)
            mydb.commit()
            c = mycursor.rowcount
            if c > 0:
                print("Deletion Done....  ")
            else:
                print('Employee Number', en, 'not found')
        except Exception as e:
            print('OOPS !!! something went wrong.\nThe Exception occured is --> ', e)


    elif choice == '6':
        try:
            en = input('Enter Employee Number of the Record to be modified ---- ')
            query ='SELECT * FROM '+ table_name +' WHERE empno='+ en
            mycursor.execute(query)
            myrecord = mycursor.fetchone()
            c = mycursor.rowcount
            if c == -1:
                print('Empno'+ en +'does not exist')
            else:
                mname = myrecord[1]
                mjob = myrecord[2]
                mbasic = myrecord[3]
                print('Employee Number : ', myrecord[0])
                print('Name : ', myrecord[1])
                print('Job : ', myrecord[2])
                print('Basic : ', myrecord[3])
                print('DA : ', myrecord[4])
                print('HRA : ', myrecord[5])
                print('Gross : ', myrecord[6])
                print('Tax : ', myrecord[7])
                print('Net : ', myrecord[8])

                print('-----------------------')
                print('Type Value to modify below or just press ENTER for no change')


                def update_employee_data(host, username, password, database_name, table_name, empno, name, job, basic_salary):
                    try:
                        connection = mysql.connector.connect(
                            host=host,
                            user=username,
                            password=password,
                            database=database_name
                        )
                        cursor = connection.cursor()

                        query = "UPDATE {} SET name = %s, job = %s, BasicSalary = %s WHERE empno = %s".format(table_name)
                        values = (name, job, basic_salary, empno)

                        cursor.execute(query, values)
                        connection.commit()

                        print("Employee data updated successfully.")

                    except mysql.connector.Error as error:
                        print("Error while connecting to MySQL:", error)

                x = input('Enter Name ---- ')
                if len(x) > 0:
                    mname = x
                x = input('Enter Job ---- ')
                if len(x) > 0:
                    mjob = x
                x = input('Enter Basic Salary ----  ')
                if len(x) > 0:
                    mbasic = float(x)
                update_employee_data('localhost', 'root', 'sahaj', db , table_name, en, mname, mjob, mbasic)

                print('Record Modified.... ')
        except Exception as e:
            print('OOPS !!! something went wrong.\nThe Exception occured is --> ',e)


    elif choice == '7':
        try:
            query='SELECT * FROM '+ table_name
            mycursor.execute(query)
            myrecords=mycursor.fetchall()
            print("\n\n\n")
            print('*' * 95)
            print('\t\t\tEmployee Payroll')
            print("*" * 95)
            now = datetime.datetime.now()
            print("Current Date and Time:",end=' ')
            print(now.strftime("%Y-%m-%d  %H:%M:%S "))
            print()
            print("-" * 95)
            print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s'\
                  %('Empno','Name','JobBasic','DA','HRA','Gross','Tax','Net'))
            print('-' * 95)
            for rec in myrecords:
                print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%(rec))
            print('-' * 95)
        except Exception as e:
            print('OOPS !!! something went wrong.\nThe Exception occured is --> ',e)


    elif choice == '8':
        try:
            query = 'SELECT * FROM '+ table_name
            mycursor.execute(query)
            now = datetime.datetime.now()
            print("\n\n\n")
            print("-"*95)
            print("\t\t\t\t Salary Slip")
            print("-"*95)
            print("Current Date and Time: ",end=' ')
            print(now.strftime("%Y-%m-%d  %H:%M:%S"))
            myrecords = mycursor.fetchall()
            for rec in myrecords:
                print('%4d \t %-15s \t %-10s \t%8.2f \t%8.2f \t%8.2f \t%9.2f \t%8.2f \t%9.2f'%rec)
        except Exception as e:
            print('OOPS !!! something went wrong.\nThe Exception occured is --> ',e)

    elif choice == '9':
        try:
            en = input("Enter Employee Number whose PaySlip you want to retrieve ---- ")
            query = 'SELECT * FROM '+ table_name +' WHERE empno='+ en
            mycursor.execute(query)
            now=datetime.datetime.now()
            print("\n\n\n\t\t\t\t Salary Slip")
            print("Current Date and Time: ",end=' ')
            print(now.strftime("%Y-%m-%d  %H:%M:%S"))
            print(tabulate(mycursor, headers=['EmpNo','Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary'], tablefmt='psql'))
        except:
            print("OOPS !!! something went wrong. Try again.... ")

    elif choice == '10':
        break

    else:
        print("Please choose a Valid Number")

        

    
