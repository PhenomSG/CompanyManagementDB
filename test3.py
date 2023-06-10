import mysql.connector

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

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

# Provide the MySQL connection details, database name, table name, and employee data
host = "localhost"
username = "root"
password = "sahaj"
database_name = "sahaj"
table_name = "moneyy"
empno = 1
name = "John Doe"
job = "Manager"
basic_salary = 5000.0

update_employee_data(host, username, password, database_name, table_name, empno, name, job, basic_salary)
