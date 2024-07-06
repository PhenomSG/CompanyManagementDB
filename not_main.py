import mysql.connector
import datetime
from tabulate import tabulate

# using functions

'''def get_database_connection(host, username, password, db=None):
    return mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=db
    ) if db else mysql.connector.connect(
        host=host,
        user=username,
        password=password
    )'''
'''
def check_database_exists(host, username, password, db):
    try:
        connection = get_database_connection(host, username, password, db)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        if result and result[0] == db:
            print(f"The database '{db}' exists.")
            return True
        else:
            print(f"The database '{db}' does not exist.")
            return False
    except mysql.connector.Error:
        print(f"The database '{db}' does not exist.")
        return False'''

def check_table_exists(connection, table_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor.fetchone()
        if result:
            print(f"The table '{table_name}' exists.")
            return True
        else:
            print(f"The table '{table_name}' does not exist.")
            return False
    except mysql.connector.Error:
        print(f"Error checking if table '{table_name}' exists.")
        return False

def create_table(cursor, table_name):
    query = f"""
    CREATE TABLE {table_name} (
        empno INT PRIMARY KEY,
        name VARCHAR(15) NOT NULL,
        job VARCHAR(15),
        BasicSalary INT,
        DA FLOAT,
        HRA FLOAT,
        GrossSalary FLOAT,
        Tax FLOAT,
        NetSalary FLOAT
    )
    """
    cursor.execute(query)
    print(f"Table {table_name} created successfully.")

def main_menu():
    print('\n' + '*'*95)
    print('\t\t\t\t MAIN MENU')
    print('*'*95)
    print('\t\t\t 1. Adding Employee Records')
    print('\t\t\t 2. Displaying Records of all Employees')
    print('\t\t\t 3. Displaying Record of a Particular Employee')
    print('\t\t\t 4. Deleting Records of all Employees')
    print('\t\t\t 5. Deleting Record of a Particular Employee')
    print('\t\t\t 6. Modifying a Record')
    print('\t\t\t 7. Displaying Payroll')
    print('\t\t\t 8. Displaying Salary Slips of all Employees')
    print('\t\t\t 9. Displaying Salary Slip of a Particular Employee')
    print('\t\t\t 10. Exit')
    print("Enter your choice: ", end='')

def add_employee(cursor, table_name):
    try:
        print("Enter Employee Information below:")
        empno = int(input('Enter Employee Number: '))
        name = input('Enter Employee Name: ')
        job = input('Enter Employee Job: ')
        basic_salary = float(input('Enter Basic Salary: '))

        if job.lower() == 'officer':
            da = basic_salary * 0.5
            hra = basic_salary * 0.35
            tax = basic_salary * 0.2
        elif job.lower() == 'manager':
            da = basic_salary * 0.45
            hra = basic_salary * 0.3
            tax = basic_salary * 0.15
        else:
            da = basic_salary * 0.4
            hra = basic_salary * 0.25
            tax = basic_salary * 0.1

        gross_salary = basic_salary + da + hra
        net_salary = gross_salary - tax

        query = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (empno, name, job, basic_salary, da, hra, gross_salary, tax, net_salary))
        mydb.commit()
        print("Record added successfully.")
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

def display_all_employees(cursor, table_name):
    try:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        print(tabulate(cursor, headers=['EmpNo', 'Name', 'Job', 'Basic Salary', 'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'], tablefmt='psql'))
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

def display_particular_employee(cursor, table_name):
    try:
        empno = input("Enter Employee Number of the record to be displayed: ")
        query = f"SELECT * FROM {table_name} WHERE empno={empno}"
        cursor.execute(query)
        record = cursor.fetchone()
        if record:
            print(tabulate([record], headers=['EmpNo', 'Name', 'Job', 'Basic Salary', 'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'], tablefmt='psql'))
        else:
            print(f"No record found for Employee Number {empno}")
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

def delete_all_employees(cursor, table_name):
    try:
        confirmation = input('Do you want to delete all the records (y/n): ')
        if confirmation.lower() == 'y':
            cursor.execute(f"DROP TABLE {table_name}")
            mydb.commit()
            print('All the records are deleted.')
            create_table(cursor, table_name)
        else:
            print('Operation cancelled.')
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

def delete_particular_employee(cursor, table_name):
    try:
        empno = input('Enter Employee Number of the record to be deleted: ')
        query = f"DELETE FROM {table_name} WHERE empno={empno}"
        cursor.execute(query)
        mydb.commit()
        if cursor.rowcount > 0:
            print("Deletion done.")
        else:
            print(f'Employee Number {empno} not found')
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

def modify_employee(cursor, table_name):
    try:
        empno = input('Enter Employee Number of the record to be modified: ')
        query = f"SELECT * FROM {table_name} WHERE empno={empno}"
        cursor.execute(query)
        record = cursor.fetchone()
        if not record:
            print(f'Employee Number {empno} does not exist')
            return

        print('Employee Number: ', record[0])
        print('Name: ', record[1])
        print('Job: ', record[2])
        print('Basic Salary: ', record[3])
        print('DA: ', record[4])
        print('HRA: ', record[5])
        print('Gross Salary: ', record[6])
        print('Tax: ', record[7])
        print('Net Salary: ', record[8])
        print('-----------------------')
        print('Type value to modify below or just press ENTER for no change')

        name = input('Enter Name: ') or record[1]
        job = input('Enter Job: ') or record[2]
        basic_salary = input('Enter Basic Salary: ') or record[3]

        query = f"UPDATE {table_name} SET name=%s, job=%s, BasicSalary=%s WHERE empno=%s"
        cursor.execute(query, (name, job, basic_salary, empno))
        mydb.commit()
        print('Record modified successfully.')
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

def display_payroll(cursor, table_name):
    try:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        records = cursor.fetchall()
        print("\n\n\n")
        print('*' * 150)
        print('\t\t\tEmployee Payroll')
        print('*' * 150)
        now = datetime.datetime.now()
        print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
        print('\n' + "-" * 150)
        print('%-5s %-15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s' % ('EmpNo', 'Name', 'Job', 'Basic Salary', 'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'))
        print('-' * 150)
        for rec in records:
            print('%4d \t%-15s \t%-10s \t%8.2f \t%8.2f \t%8.2f \t%9.2f \t%8.2f \t%9.2f' % rec)
        print('-' * 150)
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

def display_all_salary_slips(cursor, table_name):
    try:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        records = cursor.fetchall()
        now = datetime.datetime.now()
        print("\n\n\n")
        print("-" * 95)
        print("\t\t\t\t Salary Slip")
        print("-" * 95)
        print("Current Date and Time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
        for rec in records:
            print('%4d \t %-15s \t %-10s \t%8.2f \t%8.2f \t%8.2f \t%9.2f \t%8.2f \t%9.2f' % rec)
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

def display_particular_salary_slip(cursor, table_name):
    try:
        empno = input("Enter Employee Number whose PaySlip you want to retrieve: ")
        query = f"SELECT * FROM {table_name} WHERE empno={empno}"
        cursor.execute(query)
        now = datetime.datetime.now()
        print("\n\n\n\t\t\t\t Salary Slip")
        print("Current Date and Time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
        print(tabulate(cursor, headers=['EmpNo', 'Name', 'Job', 'Basic Salary', 'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'], tablefmt='psql'))
    except Exception as e:
        print(f'OOPS! Something went wrong. The exception occurred is --> {e}')

if __name__ == "__main__":
    db = input("Enter name of your Database: ")
    mydb = get_database_connection('localhost', 'root', '')

    if not check_database_exists('localhost', 'root', '', db):
        cursor = mydb.cursor()
        cursor.execute(f"CREATE DATABASE {db}")
        print(f"Successfully created database {db}")
    mydb.database = db
    cursor = mydb.cursor()

    table_name = input("\nEnter Table Name: ")
    if not check_table_exists(mydb, table_name):
        create_table(cursor, table_name)

    while True:
        main_menu()
        choice = input().strip()

        if choice == '1':
            add_employee(cursor, table_name)
        elif choice == '2':
            display_all_employees(cursor, table_name)
        elif choice == '3':
            display_particular_employee(cursor, table_name)
        elif choice == '4':
            delete_all_employees(cursor, table_name)
        elif choice == '5':
            delete_particular_employee(cursor, table_name)
        elif choice == '6':
            modify_employee(cursor, table_name)
        elif choice == '7':
            display_payroll(cursor, table_name)
        elif choice == '8':
            display_all_salary_slips(cursor, table_name)
        elif choice == '9':
            display_particular_salary_slip(cursor, table_name)
        elif choice == '10':
            break
        else:
            print("Please choose a valid number")
