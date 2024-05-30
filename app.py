import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host='localhost',  
        database='library',
        user='root',
        password='T^70)6@h*4#1S9l9l%^G'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        
        # Create a cursor object using the cursor() method
        cursor = connection.cursor()
        
        # Execute a simple query using triple quotes for multi-line strings
        query = """
        SELECT *
        FROM books b
        """
        cursor.execute(query)
        
        # Fetch all rows from the last executed statement
        records = cursor.fetchall()
        
        if records:  # Check if there are any records
            for row in records:
                print(row)
        else:
            print("No records found.")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")