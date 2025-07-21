#function to establish a connection to the database
import mysql.connector
def connection(password="321@ssaP"):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="homework_db"
    )
    print("\t \t \t \t Connection opened")
    return conn

#function to close the connection
def close_connection(conn):
    if conn.is_connected():
        conn.close()
        print("\t \t \t \t Connection closed.")
    else:
        print("\t \t \t \t Connection is already closed.")

#function to execute queries but not fetch results
def execute_query(query, params=None):
    conn = connection()
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        print("Query executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        close_connection(conn)

#function to execute queries and fetch results
def fetch_all(query, params=None):
    conn = connection()
    cursor = conn.cursor(dictionary=True)
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        if results:
            return results
        else:
            raise ValueError("No results found for your query.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        close_connection(conn)
