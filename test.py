import mysql.connector

def check_database_exists(host, username, password, database_name):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database_name
        )
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")

        result = cursor.fetchone()
        if result[0] == database_name:
            print(f"The database '{database_name}' exists.")
        else:
            print(f"The database '{database_name}' does not exist.")
        
        cursor.close()
        connection.close()
    
    except mysql.connector.Error as error:
        print(f"The database '{database_name}' does not exist.")

# Provide the MySQL connection details and database name
host = "localhost"
username = "root"
password = "sahaj"
database_name = "sas"

check_database_exists(host, username, password, database_name)
