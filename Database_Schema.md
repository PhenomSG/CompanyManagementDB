# Database Schema

## 1. Employees Table
- `emp_no`: INT (Primary Key)
- `first_name`: VARCHAR
- `last_name`: VARCHAR
- `job_title`: VARCHAR
- `net_salary`: DECIMAL
- `department_id`: INT (Foreign Key)

## 2. Departments Table
- `department_id`: INT (Primary Key)
- `department_name`: VARCHAR
- `manager_id`: INT (Foreign Key to Employees)

## 3. Projects Table
- `project_id`: INT (Primary Key)
- `project_name`: VARCHAR
- `start_date`: DATE
- `end_date`: DATE
- `department_id`: INT (Foreign Key to Departments)

## 4. Employee_Project Table (Many-to-Many Relationship)
- `emp_no`: INT (Foreign Key to Employees)
- `project_id`: INT (Foreign Key to Projects)
- `hours_worked`: DECIMAL

## 5. Salaries Table
- `emp_no`: INT (Foreign Key to Employees)
- `salary_date`: DATE
- `basic_salary`: DECIMAL
- `da`: DECIMAL
- `hra`: DECIMAL
- `gross_salary`: DECIMAL
- `tax`: DECIMAL
- `net_salary`: DECIMAL
