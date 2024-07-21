import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Darling123!",
            database="bakery"
        )
    except Error as e:
        print(f"Error: '{e}'")
    return connection

