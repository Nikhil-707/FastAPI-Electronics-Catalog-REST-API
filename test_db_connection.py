import mysql.connector
from mysql.connector import Error
from config import db_settings

def create_connection():
    """ Create a database connection to the MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=db_settings.host,
            user=db_settings.user,
            password=db_settings.password,
            database=db_settings.database
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

if __name__ == "__main__":
    connection = create_connection()
    if connection and connection.is_connected():
        connection.close()
