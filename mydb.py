import pymysql

try:
    # Connect to the MySQL server using pymysql
    dataBase = pymysql.connect(
        host='localhost',
        user='root',
        password='password123'
    )

    # Create a cursor object
    cursorObject = dataBase.cursor()

    # Create a new database
    cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

    print("Database 'elderco' created successfully!")

except pymysql.Error as err:
    print("Error: {}".format(err))

finally:
    # Close the cursor and database connection
    if 'cursorObject' in locals():
        cursorObject.close()
    if 'dataBase' in locals():
        dataBase.close()

print("ALL DONE")
