#function to establish a connection to the database
import mysql.connector
from datetime import datetime, timedelta
def today():
    return datetime.now().strftime("%Y-%m-%d") 

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
            print("No results found.")
            return []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        close_connection(conn)

def date_range(date=today()):
    dates=[]
    # Generates a list of dates that are all 7 days from today to 7 days back
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    for i in range(7):
        dates.append((date_obj - timedelta(days=i)).strftime("%Y-%m-%d"))
    return dates

def name(ID):
    # Fetches the name of the student or teacher based on their ID
    result = fetch_all(f"SELECT name FROM students WHERE id = {ID}")
    if result:
        return result[0]['name']
    else:
        result = fetch_all(f"SELECT name FROM teachers WHERE id = {ID}")
        if result:
            return result[0]['name']
        else:
            return "Unknown"

def pendinghw(id):
    results = []
    class_ = fetch_all(f"SELECT class FROM students WHERE id = {id}")[0]['class']
    for date in date_range("2023-10-01"):
        query = f"SELECT subject,title,description,due FROM `{date}` WHERE id{id} = 0 AND class = '{class_}'"
        result = fetch_all(query)
        if result:
            for item in result:
                item['date'] = date
            results.extend(result)
    return results



def update_homework_status(id, sr_no):
    results = []
    class_ = fetch_all(f"SELECT class FROM students WHERE id = {id}")[0]['class']
    num=0
    for date in date_range("2023-10-01"):
        query = f"SELECT subject,title,due,class FROM `{date}` WHERE id{id} = 0 AND class = '{class_}'"
        result = fetch_all(query)
        if result:
            for item in result:
                num += 1
                item['date'] = date
                item['sr_no'] = num
            results.extend(result)
    return results

if __name__ == "__main__":
    # Example usage
    print("Pending Homework for ID 2001:")
    pending_homework = pendinghw(2001)
    for hw in pending_homework:
        print(hw)

    print("\nUpdating Homework Status for ID 2001, Sr. No. 1:")
    updated_results = update_homework_status(2001, 1)
    for result in updated_results:
        print(result)

    print("\nName of ID 2001:", name(2001))
