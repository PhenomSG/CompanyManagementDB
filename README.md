# Payroll Management System

A comprehensive payroll management system built with Python and MySQL. The system manages employee records, departments, projects, and salary details.

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

kaam chal raha hai dheeraj rakhen

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SahajG009/Payroll-Management-System.git
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

1. Run the script:
    ```sh
    python payroll_management_system.py
    ```

2. Follow the on-screen instructions to interact with the system.

## License

This project is licensed under the [MIT License](LICENSE.md).
