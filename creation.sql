CREATE DATABASE CompanyManagementDB;
USE CompanyManagementDB;

CREATE TABLE Employees (
    emp_no INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    job_title VARCHAR(50),
    basic_salary DECIMAL(10, 2),
    department_id INT
);

CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100),
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employees(emp_no)
);

CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

CREATE TABLE Employee_Project (
    emp_no INT,
    project_id INT,
    hours_worked DECIMAL(5, 2),
    PRIMARY KEY (emp_no, project_id),
    FOREIGN KEY (emp_no) REFERENCES Employees(emp_no),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

CREATE TABLE Salaries (
    emp_no INT,
    salary_date DATE,
    basic_salary DECIMAL(10, 2),
    da DECIMAL(10, 2),
    hra DECIMAL(10, 2),
    gross_salary DECIMAL(10, 2),
    tax DECIMAL(10, 2),
    net_salary DECIMAL(10, 2),
    PRIMARY KEY (emp_no, salary_date),
    FOREIGN KEY (emp_no) REFERENCES Employees(emp_no)
);
