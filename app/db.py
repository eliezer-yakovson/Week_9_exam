import mysql.connector
from mysql.connector import Error
import os

# Simple database connection helper
# Students should NOT modify this file
# This provides a basic connection to MySQL without pooling or retries

def get_db_connection():
    """
    Returns a MySQL database connection.
    Used by dal.py functions to execute queries.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "mysql"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("MYSQL_ROOT_PASSWORD", "1234"),
            database=os.getenv("MYSQL_DATABASE", "sales_db")
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise

