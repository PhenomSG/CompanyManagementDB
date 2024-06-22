import mysql.connector

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
            print(f"The table '{table_name}' exists in the database '{database_name}'.")
        else:
            print(f"The table '{table_name}' does not exist in the database '{database_name}'.")
        
        cursor.close()
        connection.close()
    
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

# Provide the MySQL connection details, database name, and table name
host = "localhost"
username = "root"
password = ""
database_name = ""
table_name = "money"

check_table_exists(host, username, password, database_name, table_name)
