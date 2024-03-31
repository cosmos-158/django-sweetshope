import mysql.connector
import pandas as pd

def connect_to_db(s_name):
    config = {
    'user': 'root',
    'password': 'pwd',
    'host': 'localhost',
    'database': 'sweetsdb',
    'raise_on_warnings': True
    }
    price = None
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("Select * from sweets")
            rows = cursor.fetchall()
            df = pd.DataFrame(rows, columns=cursor.column_names)
            df['sweetName'] = df['sweetName'].str.strip().str.replace(' ', '').str.upper()
            price = df[df['sweetName'] == s_name]['price'].iloc[0]
            print(price)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed")
    
    return price

if __name__ == "__main__":
    query = "SELECT * FROM sweets"
    df = connect_to_db(query)
    print(df)
