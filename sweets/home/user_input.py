import mysql.connector
import pandas as pd

def insert_into_db(query):
    config = {
    'user': 'root',
    'password': 'enter password here',
    'host': 'localhost',
    'database': 'sweetsdb',
    'raise_on_warnings': True
    }

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print(query)
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("Data Inserted")
            cursor.execute("Select * from user_detail")
            rows = cursor.fetchall()
            print(rows)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed")


if __name__ == "__main__":
    query = "SELECT * FROM user_detail"
    insert_into_db(query)
    
