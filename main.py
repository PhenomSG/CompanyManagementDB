# Importing Dependencies

import mysql.connector as ms
import datetime
from tabulate import tabulate
from connection import is_connected, get_database_connection

# Establishing Connection
flag = is_connected()
print(flag)

# Database to be used
db = "company"
print(f"Using {db} Database")
print(f"All actions will happen inside {db} database")

if flag:
    try:
        # Cheking if connected
        connection = get_database_connection()
        cursor = connection.cursor()

        # Selecting the database
        cursor.execute(f"USE {db};")
        print(f"Database changed to {db}")

        # Sample query to test the connection
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Tables in the database:", tables)
        
        # Write other code here
        
    except ms.Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
else:
    print("Failed to connect to MySQL")
