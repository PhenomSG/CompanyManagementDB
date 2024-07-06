# Importing Dependencies
import mysql.connector as ms
import datetime
from tabulate import tabulate
from connection import is_connected, get_database_connection

# Establishing Connection
flag = is_connected()
print(flag)

# Database to be used
db = "CompanyManagementDB"
tables = ["employees","departments","projects","employee_project","salaries"]
print(f"Using {db} Database")
print(f"All actions will happen inside {db} database")

if flag:
    try:
        # Checking if connected
        connection = get_database_connection()
        cursor = connection.cursor()

        # Selecting the database
        cursor.execute(f"USE {db};")
        print(f"Database changed to {db}")

        # Sample query to test the connection
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in the database:", tables)
        
        # Function to insert data into a table
        def insert_data():
            table_name = input("Enter the table name to insert data into: ")
            if table_name.lower() == "employees":
                emp_no = int(input("Enter employee number: "))
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                job_title = input("Enter job title: ")
                basic_salary = float(input("Enter basic salary: "))
                department_id = int(input("Enter department id: "))
                query = "INSERT INTO Employees (emp_no, first_name, last_name, job_title, basic_salary, department_id) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (emp_no, first_name, last_name, job_title, basic_salary, department_id)
            
            # skeleton made
            
            cursor.execute(query, values)
            connection.commit()
            print(f"Data inserted into {table_name} table successfully.")

        # Function to update data in a table
        def update_data():
            table_name = input("Enter the table name to update data: ")
            if table_name.lower() == "employees":
                emp_no = int(input("Enter the employee number to update: "))
                column_name = input("Enter the column name to update: ")
                new_value = input("Enter the new value: ")
                query = f"UPDATE Employees SET {column_name} = %s WHERE emp_no = %s"
                values = (new_value, emp_no)
            
            # skeleton made
            
            cursor.execute(query, values)
            connection.commit()
            print(f"Data in {table_name} table updated successfully.")

        # Function to delete data from a table
        def delete_data():
            table_name = input("Enter the table name to delete data from: ")
            if table_name.lower() == "employees":
                emp_no = int(input("Enter the employee number to delete: "))
                query = "DELETE FROM Employees WHERE emp_no = %s"
                values = (emp_no,)
            
            # skeleton made
            
            cursor.execute(query, values)
            connection.commit()
            print(f"Data deleted from {table_name} table successfully.")

        # Main menu
        def main_menu():
            print('\n' + '*'*95)
            print('\t\t\t\t MAIN MENU')
            print('*'*95)
            print('\t\t\t 1. Insert data into table')
            print('\t\t\t 2. Update data in table')
            print('\t\t\t 3. Delete data from table')
            print('\t\t\t 4. Exit')
            print("Enter your choice: ", end='')

        # Write other code here
        while True:
            main_menu()
            choice = input().strip()

            if choice == '1':
                insert_data()
            elif choice == '2':
                update_data()
            elif choice == '3':
                delete_data()
            elif choice == '4':
                break
            else:
                print("Please choose a valid number")

    except ms.Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
else:
    print("Failed to connect to MySQL")
