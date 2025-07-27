import mysql.connector
from datetime import date, datetime, timedelta
import os,platform

def today():
    """Returns today's date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d") 

password,user='pass','root'

def get_credentials_path():
    """Returns the path to the credentials.txt file used for DB login."""
    folder = os.getcwd()
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, 'credentials.txt')

try:
    with open(get_credentials_path(), 'r') as file:
        for line in file:
            user, password = line.strip().split(':')
except:
    print("Look's like the text file storing credentials is missing or displaced. Please run Intallation_Wizard.py using `python -m Installation_Wizard`")

def connection(password=password,user=user):
    """Establishes and returns a connection to the MySQL database."""
    conn = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database="School_Management_Database"
    )
    return conn

#function to close the connection
def close_connection(conn):
    """Closes the given database connection if it's open."""
    if conn.is_connected():
        conn.close()

#function to execute queries but not fetch results
def execute_query(query, params=None):
    """Executes a write/query statement (INSERT, UPDATE, DELETE) on the DB."""
    conn = connection()
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        close_connection(conn)

#function to execute queries and fetch results
def fetch_all(query, params=None):
    """Executes a SELECT query and returns all results as a list of dicts."""
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
            return []
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        close_connection(conn)

def date_range(date=today()):
    """Returns a list of 7 dates from today backward in YYYY-MM-DD format."""
    dates=[]
    # Generates a list of dates that are all 7 days from today to 7 days back
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    for i in range(7):
        dates.append((date_obj - timedelta(days=i)).strftime("%Y-%m-%d"))
    return dates

def name(ID):
    """Fetches the name of a student or teacher based on their ID."""
    result = fetch_all(f"SELECT name FROM students WHERE id = {ID}")
    if result:
        return result[0]['name']
    else:
        result = fetch_all(f"SELECT name FROM teachers WHERE id = {ID}")
        if result:
            return result[0]['name']
        else:
            return ID
    
def pendinghw(id):
    """Fetches all pending homeworks for a student based on their ID."""
    results = []
    class_ = fetch_all(f"SELECT class FROM students WHERE id = {id}")[0]['class']
    for date in date_range(today()):
        query = f"SELECT subject,title,description,due FROM `{date}` WHERE id{id} = 0 AND class = '{class_}'"
        result = fetch_all(query)
        if result:
            for item in result:
                item['date'] = date
            results.extend(result)
    return results

def update_homework_status(id, sr_no):
    """Prepares the list of homeworks eligible for status update based on student ID."""
    results = []
    class_ = fetch_all(f"SELECT class FROM students WHERE id = {id}")[0]['class']
    num1=0
    for date in date_range(today()):
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
    """Adds a new homework to the specified date's table."""
    subject = fetch_all(f"SELECT subject FROM teachers WHERE id = {teacher_id}")[0]['subject']
    query = f"INSERT INTO `{date}` (teacher_id, title, class, description, due, subject) VALUES (%s, %s, %s, %s, %s, %s)"
    params = (teacher_id, title, class_, description, due, subject)
    execute_query(query, params)

def show_homework(id):
    """Returns all homeworks assigned by a teacher given their ID."""
    results = []
    subject = fetch_all(f"SELECT subject FROM teachers WHERE id = {id}")[0]['subject']
    num2=0
    for date in date_range(today()):
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
    """Calculates homework completion percentage for the class handled by a teacher."""
    results = []
    class_ = fetch_all(f"SELECT class FROM teachers WHERE id = {id}")[0]['class']
    query = f"SELECT id FROM students WHERE class = '{class_}'"
    students = fetch_all(query)
    total_students = len(students)
    no_of_submissions,submission,percent_completed = 0,0,0
    for student in students:
        for date in date_range(today()):
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
    """Fetches all homeworks and their completion status for a given student."""
    results = []
    query = f"SELECT id FROM students WHERE name = '{name}' AND class = '{class_}'"
    student_id = fetch_all(query)
    if not student_id:
        return results
    student_id = student_id[0]['id']
    for date in date_range(today()):
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
    """Returns list of all students with completed homework stats."""
    results = fetch_all("SELECT id, name, DOB, class, address FROM students")
    completed_hws=0
    for result in results:
        for date in date_range(today()):
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
    """Returns list of teachers with homework assignment stats."""
    results = fetch_all("SELECT id, name, subject, class, address FROM teachers")
    assigned_hws=0
    for result in results:
        for date in date_range(today()):
            query = f"SELECT teacher_id FROM `{date}` WHERE teacher_id = {result['id']}"
            hw_result = fetch_all(query)
            if hw_result:
                assigned_hws += 1
        result['assigned_hw'] = assigned_hws
        result['overall_percent'] = class_homework_status(result['id'])[0]['percent_completed']
        assigned_hws = 0
    return results

def add_student(id, name, dob, class_, address):
    """Adds a student record to the students table."""
    query = "INSERT INTO students (id, name, DOB, class, address) VALUES (%s, %s, %s, %s, %s)"
    params = (id, name, dob, class_, address)
    execute_query(query, params)

def add_teacher(id, name, subject, class_, address):
    """Adds a teacher record to the teachers table."""
    query = "INSERT INTO teachers (id, name, subject, class, address) VALUES (%s, %s, %s, %s, %s)"
    params = (id, name, subject, class_, address)
    execute_query(query, params)
    
def update_student(id, name, dob, class_, address):
    """Updates a student record in the students table."""
    query = "UPDATE students SET name = %s, DOB = %s, class = %s, address = %s WHERE id = %s"
    params = (name, dob, class_, address, id)
    execute_query(query, params)

def update_teacher(id, name, subject, class_, address):
    """Updates a teacher record in the teachers table."""
    query = "UPDATE teachers SET name = %s, subject = %s, class = %s, address = %s WHERE id = %s"
    params = (name, subject, class_, address, id)
    execute_query(query, params)

def all_class_status():
    """Returns homework completion stats for all classes handled by teachers."""
    results = []
    teacher_ids = fetch_all("SELECT id FROM teachers")
    for teacher_id in teacher_ids:
        class_status = class_homework_status(teacher_id['id'])
        if class_status:
            results.append(class_status[0])
    return results

def all_teacher_status():
    """Returns overall homework stats for all teachers."""
    results = []
    total_hw = 0
    teacher_ids = fetch_all("SELECT id FROM teachers")
    for teacher_id in teacher_ids:
        for date in date_range(today()):
            query = f"SELECT COUNT(*) as total_hw FROM `{date}` WHERE teacher_id = {teacher_id['id']}"
            hw = fetch_all(query)[0]['total_hw']
            total_hw += hw
        class_status = class_homework_status(teacher_id['id'])
        if class_status:
            results.append({'percent_completed': class_status[0]['percent_completed'],
                             'teacher_id': teacher_id['id'],
                               'total_hw': total_hw,
                               'name': name(teacher_id['id'])})
    return results
