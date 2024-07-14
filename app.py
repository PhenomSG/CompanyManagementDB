import streamlit as st
import mysql.connector as ms
from connection import is_connected, get_database_connection
from tabulate import tabulate
import pandas as pd

# Function to establish connection
def establish_connection():
    flag = is_connected()
    if flag:
        try:
            connection = get_database_connection()
            return connection
        except ms.Error as e:
            st.error(f"Error: {e}")
    else:
        st.error("Failed to connect to MySQL")
    return None

# Insert data function for Streamlit
def insert_data(connection):
    db_tables = ["employees", "departments", "projects", "employee_project", "salaries"]
    table_name = st.selectbox("Select the table to insert data into:", db_tables)
    cursor = connection.cursor()

    if table_name == "employees":
        emp_no = st.number_input("Enter employee number:", min_value=1, step=1)
        first_name = st.text_input("Enter first name:")
        last_name = st.text_input("Enter last name:")
        job_title = st.text_input("Enter job title:")
        basic_salary = st.number_input("Enter basic salary:", min_value=0.0, step=0.01)
        department_id = st.number_input("Enter department id:", min_value=1, step=1)
        if st.button("Insert"):
            query = "INSERT INTO Employees (emp_no, first_name, last_name, job_title, basic_salary, department_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (emp_no, first_name, last_name, job_title, basic_salary, department_id)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data inserted into employees table successfully.")

    elif table_name == "departments":
        department_id = st.number_input("Enter department id:", min_value=1, step=1)
        department_name = st.text_input("Enter department name:")
        manager_id = st.number_input("Enter manager id:", min_value=1, step=1)
        if st.button("Insert"):
            query = "INSERT INTO Departments (department_id, department_name, manager_id) VALUES (%s, %s, %s)"
            values = (department_id, department_name, manager_id)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data inserted into departments table successfully.")

    elif table_name == "projects":
        project_id = st.number_input("Enter project id:", min_value=1, step=1)
        project_name = st.text_input("Enter project name:")
        start_date = st.date_input("Enter start date:")
        end_date = st.date_input("Enter end date:")
        department_id = st.number_input("Enter department id:", min_value=1, step=1)
        if st.button("Insert"):
            query = "INSERT INTO Projects (project_id, project_name, start_date, end_date, department_id) VALUES (%s, %s, %s, %s, %s)"
            values = (project_id, project_name, start_date, end_date, department_id)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data inserted into projects table successfully.")

    elif table_name == "employee_project":
        emp_no = st.number_input("Enter employee number:", min_value=1, step=1)
        project_id = st.number_input("Enter project id:", min_value=1, step=1)
        hours_worked = st.number_input("Enter hours worked:", min_value=0.0, step=0.01)
        if st.button("Insert"):
            query = "INSERT INTO Employee_Project (emp_no, project_id, hours_worked) VALUES (%s, %s, %s)"
            values = (emp_no, project_id, hours_worked)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data inserted into employee_project table successfully.")

    elif table_name == "salaries":
        emp_no = st.number_input("Enter employee number:", min_value=1, step=1)
        salary_date = st.date_input("Enter salary date:")
        basic_salary = st.number_input("Enter basic salary:", min_value=0.0, step=0.01)
        if st.radio("Is the Employee's residence rented?", ('Yes', 'No')) == 'Yes':
            fda, fhra = 0.5, 0.4
        else:
            fda, fhra = 0.5, 0
        da = fda * basic_salary
        hra = fhra * basic_salary
        gross_salary = basic_salary + da + hra
        taxable_income = gross_salary - basic_salary
        if taxable_income <= 250000:
            tax = 0
        elif taxable_income <= 500000:
            tax = 0.05 * (taxable_income - 250000)
        elif taxable_income <= 1000000:
            tax = 12500 + 0.2 * (taxable_income - 500000)
        else:
            tax = 112500 + 0.3 * (taxable_income - 1000000)
        net_salary = gross_salary - tax
        if st.button("Insert"):
            query = "INSERT INTO Salaries (emp_no, salary_date, basic_salary, da, hra, gross_salary, tax, net_salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (emp_no, salary_date, basic_salary, da, hra, gross_salary, tax, net_salary)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data inserted into salaries table successfully.")

# Update data function for Streamlit
def update_data(connection):
    db_tables = ["employees", "departments", "projects", "employee_project", "salaries"]
    table_name = st.selectbox("Select the table to update data in:", db_tables)
    cursor = connection.cursor()

    if table_name == "employees":
        emp_no = st.number_input("Enter the employee number to update:", min_value=1, step=1)
        column_name = st.text_input("Enter the column name to update:")
        new_value = st.text_input("Enter the new value:")
        if st.button("Update"):
            query = f"UPDATE Employees SET {column_name} = %s WHERE emp_no = %s"
            values = (new_value, emp_no)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data in employees table updated successfully.")

    elif table_name == "departments":
        department_id = st.number_input("Enter the department id to update:", min_value=1, step=1)
        column_name = st.text_input("Enter the column name to update:")
        new_value = st.text_input("Enter the new value:")
        if st.button("Update"):
            query = f"UPDATE Departments SET {column_name} = %s WHERE department_id = %s"
            values = (new_value, department_id)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data in departments table updated successfully.")

    elif table_name == "projects":
        project_id = st.number_input("Enter the project id to update:", min_value=1, step=1)
        column_name = st.text_input("Enter the column name to update:")
        new_value = st.text_input("Enter the new value:")
        if st.button("Update"):
            query = f"UPDATE Projects SET {column_name} = %s WHERE project_id = %s"
            values = (new_value, project_id)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data in projects table updated successfully.")

    elif table_name == "employee_project":
        emp_no = st.number_input("Enter the employee number to update:", min_value=1, step=1)
        project_id = st.number_input("Enter the project id to update:", min_value=1, step=1)
        column_name = st.text_input("Enter the column name to update:")
        new_value = st.text_input("Enter the new value:")
        if st.button("Update"):
            query = f"UPDATE Employee_Project SET {column_name} = %s WHERE emp_no = %s AND project_id = %s"
            values = (new_value, emp_no, project_id)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data in employee_project table updated successfully.")

    elif table_name == "salaries":
        emp_no = st.number_input("Enter the employee number to update:", min_value=1, step=1)
        salary_date = st.date_input("Enter the salary date to update:")
        column_name = st.text_input("Enter the column name to update:")
        new_value = st.text_input("Enter the new value:")
        if st.button("Update"):
            query = f"UPDATE Salaries SET {column_name} = %s WHERE emp_no = %s AND salary_date = %s"
            values = (new_value, emp_no, salary_date)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data in salaries table updated successfully.")

# Delete data function for Streamlit
def delete_data(connection):
    db_tables = ["employees", "departments", "projects", "employee_project", "salaries"]
    table_name = st.selectbox("Select the table to delete data from:", db_tables)
    cursor = connection.cursor()

    if table_name == "employees":
        emp_no = st.number_input("Enter the employee number to delete:", min_value=1, step=1)
        if st.button("Delete"):
            query = "DELETE FROM Employees WHERE emp_no = %s"
            values = (emp_no,)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data deleted from employees table successfully.")

    elif table_name == "departments":
        department_id = st.number_input("Enter the department id to delete:", min_value=1, step=1)
        if st.button("Delete"):
            query = "DELETE FROM Departments WHERE department_id = %s"
            values = (department_id,)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data deleted from departments table successfully.")

    elif table_name == "projects":
        project_id = st.number_input("Enter the project id to delete:", min_value=1, step=1)
        if st.button("Delete"):
            query = "DELETE FROM Projects WHERE project_id = %s"
            values = (project_id,)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data deleted from projects table successfully.")

    elif table_name == "employee_project":
        emp_no = st.number_input("Enter the employee number to delete:", min_value=1, step=1)
        project_id = st.number_input("Enter the project id to delete:", min_value=1, step=1)
        if st.button("Delete"):
            query = "DELETE FROM Employee_Project WHERE emp_no = %s AND project_id = %s"
            values = (emp_no, project_id)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data deleted from employee_project table successfully.")

    elif table_name == "salaries":
        emp_no = st.number_input("Enter the employee number to delete:", min_value=1, step=1)
        salary_date = st.date_input("Enter the salary date to delete:")
        if st.button("Delete"):
            query = "DELETE FROM Salaries WHERE emp_no = %s AND salary_date = %s"
            values = (emp_no, salary_date)
            cursor.execute(query, values)
            connection.commit()
            st.success("Data deleted from salaries table successfully.")

# Generate payslip function for Streamlit
def generate_payslip(connection):
    emp_no = st.number_input("Enter the employee number:", min_value=1, step=1)
    salary_date = st.date_input("Enter the salary date:")
    cursor = connection.cursor()

    query = """
        SELECT emp_no, salary_date, basic_salary, da, hra, gross_salary, tax, net_salary
        FROM Salaries
        WHERE emp_no = %s AND salary_date = %s
    """
    values = (emp_no, salary_date)

    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        emp_no, salary_date, basic_salary, da, hra, gross_salary, tax, net_salary = result

        data = [
            ["Employee Number:", emp_no],
            ["Salary Date:", salary_date],
            ["Basic Salary:", basic_salary],
            ["DA:", da],
            ["HRA:", hra],
            ["Gross Salary:", gross_salary],
            ["Tax:", tax],
            ["Net Salary:", net_salary],
        ]

        st.write("\n" + "*" * 30)
        st.write("PAYSLIP")
        st.write("*" * 30)
        st.table(data)
        st.write("*" * 30)
    else:
        st.error("No payslip found for the given employee number and salary date.")

# Display table contents function for Streamlit
def display_table_contents(connection):
    db_tables = ["employees", "departments", "projects", "employee_project", "salaries"]
    table_name = st.selectbox("Select the table to display data:", db_tables)
    cursor = connection.cursor()

    query = f"SELECT * FROM {table_name}"

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if not rows:
            st.warning(f"No data found in {table_name} table.")
            return
        
        column_names = [i[0] for i in cursor.description]
        st.write(f"\nContents of {table_name} Table:")
        st.table(pd.DataFrame(rows, columns=column_names))
        
    except ms.Error as e:
        st.error(f"Error fetching data from {table_name} table: {e}")

# Streamlit app layout
def main():
    st.title("Company Management System")
    connection = establish_connection()
    
    if connection:
        st.sidebar.title("Actions")
        option = st.sidebar.selectbox("Select an action:", ["Insert Data", "Update Data", "Delete Data", "Generate Payslip", "Display Table Contents", "Exit"])
        
        if option == "Insert Data":
            insert_data(connection)
        elif option == "Update Data":
            update_data(connection)
        elif option == "Delete Data":
            delete_data(connection)
        elif option == "Generate Payslip":
            generate_payslip(connection)
        elif option == "Display Table Contents":
            display_table_contents(connection)
        elif option == "Exit":
            st.write("Thank you for using the Company Management System.")
        
        if connection.is_connected():
            connection.close()

if __name__ == '__main__':
    main()
