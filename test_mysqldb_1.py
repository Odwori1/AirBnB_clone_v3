import MySQLdb

# MySQL database connection parameters
MYSQL_USER = 'root'
MYSQL_PASSWORD = '0791486006@ubuntu'
MYSQL_HOST = 'localhost'
MYSQL_DB = 'new_db'

try:
    # Connect to the MySQL database
    conn = MySQLdb.connect(
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        db=MYSQL_DB
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a simple SQL query to retrieve the current MySQL version
    cursor.execute("SELECT VERSION()")

    # Fetch the result
    mysql_version = cursor.fetchone()[0]

    # Print the MySQL version
    print("MySQL version:", mysql_version)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except MySQLdb.Error as e:
    print("Error connecting to MySQL:", e)

