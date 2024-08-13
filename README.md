# Payroll Management System

A comprehensive payroll management system built with Python, Streamlit, and MySQL. The system manages employee records, departments, projects, and salary details.

## Database Schema

### 1. Employees Table
- `emp_no`: INT (Primary Key)
- `first_name`: VARCHAR
- `last_name`: VARCHAR
- `job_title`: VARCHAR
- `basic_salary`: DECIMAL
- `department_id`: INT (Foreign Key)

### 2. Departments Table
- `department_id`: INT (Primary Key)
- `department_name`: VARCHAR
- `manager_id`: INT (Foreign Key to Employees)

### 3. Projects Table
- `project_id`: INT (Primary Key)
- `project_name`: VARCHAR
- `start_date`: DATE
- `end_date`: DATE
- `department_id`: INT (Foreign Key to Departments)

### 4. Employee_Project Table (Many-to-Many Relationship)
- `emp_no`: INT (Foreign Key to Employees)
- `project_id`: INT (Foreign Key to Projects)
- `hours_worked`: DECIMAL

### 5. Salaries Table
- `emp_no`: INT (Foreign Key to Employees)
- `salary_date`: DATE
- `basic_salary`: DECIMAL
- `da`: DECIMAL
- `hra`: DECIMAL
- `gross_salary`: DECIMAL
- `tax`: DECIMAL
- `net_salary`: DECIMAL

## Features

### Database Connectivity and Setup

- Establishes connection to the MySQL database.
- Selects the `CompanyManagementDB` database for operations.
- Lists available tables (`employees`, `departments`, `projects`, `employee_project`, `salaries`).

### Data Manipulation Functions

- **Insert Data into Tables**
  - Allows insertion of records into tables such as `employees`, `departments`, `projects`, `employee_project`, and `salaries`.
  - Automatically calculates DA, HRA, gross salary, tax, and net salary based on predefined formulas for salary insertions.

- **Update Data in Tables**
  - Provides functionality to update existing records in tables like `employees`, `departments`, `projects`, `employee_project`, and `salaries`.
  - Allows updating specific columns identified by the user.

- **Delete Data from Tables**
  - Enables deletion of records from tables such as `employees`, `departments`, `projects`, `employee_project`, and `salaries`.
  - Prompts for identification using primary keys (`emp_no`, `department_id`, `project_id`, etc.).

### Payslip Generation

- **Generate Payslip**
  - Fetches and displays payslip details for a specific employee and salary date.
  - Calculates and displays components like basic salary, DA, HRA, gross salary, tax, and net salary in a formatted table using the `tabulate` library.

### User Interface

- **Streamlit Application**
  - Provides a user-friendly web interface with options to insert, update, delete data, generate payslips, and view other functionalities.
  - Ensures intuitive navigation through the system functionalities.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/PhenomSG/Payroll-Management-System.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Payroll-Management-System
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure the MySQL database connection in the script.

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run streamlit_app.py
    ```

2. Open your web browser and go to the provided URL to interact with the application.

## License

This project is licensed under the [MIT License](LICENSE.md).
