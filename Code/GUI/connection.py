#function to establish a connection to the database
import mysql.connector
from datetime import date, datetime, timedelta
def today():
    return datetime.now().strftime("%Y-%m-%d") 

def connection(password="321@ssaP"):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="homework_db"
    )
    return conn

#function to close the connection
def close_connection(conn):
    if conn.is_connected():
        conn.close()

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
    num1=0
    for date in date_range("2023-10-01"):
        query = f"SELECT subject,title,due,class FROM `{date}` WHERE id{id} = 0 AND class = '{class_}'"
        result = fetch_all(query)
        if result:
            for item in result:
                num1 += 1
                item['date'] = date
                item['sr_no'] = num1
            results.extend(result)
    return results

def add_homework(date,teacher_id, title, class_, description, due):
    subject = fetch_all(f"SELECT subject FROM teachers WHERE id = {teacher_id}")[0]['subject']
    query = f"INSERT INTO `{date}` (teacher_id, title, class, description, due, subject) VALUES (%s, %s, %s, %s, %s, %s)"
    params = (teacher_id, title, class_, description, due, subject)
    execute_query(query, params)

def show_homework(id):
    results = []
    subject = fetch_all(f"SELECT subject FROM teachers WHERE id = {id}")[0]['subject']
    num2=0
    for date in date_range("2023-10-02"):
        query = f"SELECT title,description,due,sr_no,class FROM `{date}` WHERE teacher_id = {id}"
        result = fetch_all(query)
        if result:
            for item in result:
                num2 += 1
                item['index'] = num2
                item['date'] = date
                item['subject'] = subject
                item['teacher_id'] = id
            results.extend(result)
    return results


def class_homework_status(id):
    results = []
    class_ = fetch_all(f"SELECT class FROM teachers WHERE id = {id}")[0]['class']
    query = f"SELECT id FROM students WHERE class = '{class_}'"
    students = fetch_all(query)
    total_students = len(students)
    no_of_submissions,submission,percent_completed = 0,0,0
    for student in students:
        for date in date_range("2023-10-02"):
            query = f"SELECT id{student['id']} FROM `{date}` WHERE class = '{class_}'"
            result = fetch_all(query)
            if result:
                no_of_submissions = sum(1 for item in result if item[f'id{student["id"]}'] == 1)
        submission += no_of_submissions
    percent_completed = (submission / total_students) * 100 if total_students > 0 else 0
    results.append({
        'class': class_,
        'total_students': total_students,
        'no_of_submissions': submission,
        'percent_completed': f"{percent_completed:.2f}%"
    })
    return results

def individual_homework_status(name,class_):
    results = []
    query = f"SELECT id FROM students WHERE name = '{name}' AND class = '{class_}'"
    student_id = fetch_all(query)
    if not student_id:
        return results
    student_id = student_id[0]['id']
    for date in date_range("2023-10-02"):
        query = f"SELECT id{student_id} as status, title, due FROM `{date}` WHERE class = '{class_}'"
        result = fetch_all(query)
        if result:
            for item in result:
               item['date'] = date
               item['name'] = name
               item['status'] = "Completed" if item['status'] == 1 else "Pending"
            results.extend(result)
    return results

def show_students():
    results = fetch_all("SELECT id, name, DOB, class, address FROM students")
    completed_hws=0
    for result in results:
        for date in date_range("2023-10-02"):
            try:
                query = f"SELECT id{result['id']} FROM `{date}` WHERE class = '{result['class']}'"
                hw_result = fetch_all(query)[0][f'id{result["id"]}']
                if hw_result == 1:
                    completed_hws += 1
            except IndexError:
                pass
        result['completed_hw'] = completed_hws
        result['overall_percent'] = f"{(completed_hws / 7) * 100:.2f}%" if completed_hws > 0 else "0%"
        completed_hws = 0
    return results

def show_teachers():
    results = fetch_all("SELECT id, name, subject, class, address FROM teachers")
    assigned_hws=0
    for result in results:
        for date in date_range("2023-10-02"):
            query = f"SELECT teacher_id FROM `{date}` WHERE teacher_id = {result['id']}"
            hw_result = fetch_all(query)
            if hw_result:
                assigned_hws += 1
        result['assigned_hw'] = assigned_hws
        result['overall_percent'] = class_homework_status(result['id'])[0]['percent_completed']
        assigned_hws = 0
    return results

def add_student(id, name, dob, class_, address):
    query = "INSERT INTO students (id, name, DOB, class, address) VALUES (%s, %s, %s, %s, %s)"
    params = (id, name, dob, class_, address)
    execute_query(query, params)

def add_teacher(id, name, subject, class_, address):
    query = "INSERT INTO teachers (id, name, subject, class, address) VALUES (%s, %s, %s, %s, %s)"
    params = (id, name, subject, class_, address)
    execute_query(query, params)
    
def update_student(id, name, dob, class_, address):
    query = "UPDATE students SET name = %s, DOB = %s, class = %s, address = %s WHERE id = %s"
    params = (name, dob, class_, address, id)
    execute_query(query, params)

def update_teacher(id, name, subject, class_, address):
    query = "UPDATE teachers SET name = %s, subject = %s, class = %s, address = %s WHERE id = %s"
    params = (name, subject, class_, address, id)
    execute_query(query, params)


if __name__ == "__main__":
    # Example usage
    # print("Pending Homework for ID 2001:")
    # pending_homework = pendinghw(2001)
    # for hw in pending_homework:
    #     print(hw)

    # print("\nUpdating Homework Status for ID 2001, Sr. No. 1:")
    # updated_results = update_homework_status(2001, 1)
    # for result in updated_results:
    #     print(result)

    # print("\nAdding Homework for Teacher ID 5001:")
    # add_homework(date='2023-10-02', teacher_id=5001, title='Math Assignment', class_='10A', description='Solve exercises 1 to 10', due='2023-10-09')
    # print("Homework added successfully.")

    # print("\nName of ID 2001:", name(2001))

    #Check show_homework function
    # show_homework = show_homework(5003)
    # for hw in show_homework:
    #     print(hw)

    #Check class_homework_status function
    # class_status = class_homework_status(5003)
    # for status in class_status:
    #     print(status)

    #Check individual_homework_status function
    # individual_status = individual_homework_status("Sneha Patel", "10C")
    # for status in individual_status:
    #     print(status)

    #Check show_students function
    # students = show_students()
    # for student in students:
    #     print(student)

    #Check add_student function
    # add_student('2021', 'John Doe', '2005-05-15', '10A', '123 Main St')

    #Check update_student function
    update_student('2021', 'John Doe', '2005-05-15', '10A', '456 Elm St')
