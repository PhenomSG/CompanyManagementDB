# Payroll-Management-System

A payroll management system is a software application or a set of processes designed to automate and streamline the process of managing employee payroll. 

It typically involves calculating and disbursing employee salaries, tracking attendance, managing tax deductions, and generating pay slips.

The provided code represents a basic implementation of a payroll management system in Python using a MySQL database. 

# Here is an overview of its functionality:

**1. Database and Table Creation:**
   - The code establishes a connection to a MySQL database and creates a database (if it doesn't exist) based on user input.
   - It creates a table (if it doesn't exist) to store employee records. The table structure includes columns for employee information such as employee number, name, job, salary details, and more.

**2. User Interaction:**
   - The code presents a menu-driven interface to interact with the payroll system.
   - The user is prompted to choose from various options like adding employee records, displaying records, modifying records, generating salary slips, and more.

**3. Adding Employee Records:**
   - When the user selects the option to add employee records, they are prompted to enter information about the employee, such as employee number, name, job, and basic salary.
   - Based on the job category, the code calculates additional components like DA (Dearness Allowance), HRA (House Rent Allowance), gross salary, tax, and net salary.
   - The employee record is then inserted into the database table.

**4. Displaying and Modifying Records:**
   - The code provides options to display records of all employees or a specific employee.
   - If the user chooses to display a specific employee's record, they need to provide the employee number, and the corresponding record is fetched from the database and displayed.
   - There is also an option to modify a specific employee's record, where the user can update information like name, job, or basic salary.

**5. Deleting Records:**
   - The code provides options to delete records of all employees or a specific employee.
   - When deleting records, the user is asked for confirmation before proceeding.

**6. Generating Payroll and Salary Slips:**
   - The code includes options to generate employee payroll and salary slips.
   - Payroll generation fetches all employee records from the database and displays them along with relevant salary details.
   - Salary slip generation allows the user to either generate slips for all employees or a specific employee.

**7. Error Handling:**
   - The code includes exception handling to catch and display any errors that may occur during database operations or user input.
