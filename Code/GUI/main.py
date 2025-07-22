from textual.app import App
from login import WelcomeScreen, LoginScreen, IDScreen, User, ID
from connection import connection, close_connection, today, date_range

connection()

class HomeworkApp(App):
    CSS = """
    #title {
        text-align: center;
        text-style: bold;
        margin: 2;
    }
    #authors {
        text-align: center;
        color: blue;
    }
    #welcome-container, #login-container, #id-container {
        align: center middle;
        height: 100%;
    }
    #login-title {
        text-style: bold;
        margin-bottom: 1;
    }
    #id_note {
        color: green;
        margin-top: 1;
    }
    """

    role: str = "Student"

    def on_mount(self) -> None:
        self.install_screen(WelcomeScreen(), name="welcome")
        self.install_screen(LoginScreen(), name="login")
        self.install_screen(IDScreen(), name="id")
        self.push_screen("welcome")

if __name__ == "__main__":

    for date in date_range(today()):
        cursor = connection.connection().cursor()
        cursor.execute("SELECT id FROM students")
        student_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()

        # Build the CREATE TABLE query dynamically
        columns = """
        sr_no INT AUTO_INCREMENT PRIMARY KEY,
        class VARCHAR(50),
        teacher_id VARCHAR(50),
        subject VARCHAR(100),
        title VARCHAR(100),
        description VARCHAR(500),
        due DATE
    """
        for student_id in student_ids:
            columns += f",\n    id{student_id} BOOLEAN DEFAULT FALSE"

        query = f"""
    CREATE TABLE IF NOT EXISTS `{date}` (
    {columns}
    );
        """
        # Execute the query to create the table
        cursor = connection.connection().cursor()
        cursor.execute(query)
        cursor.close()

    import login
    result = HomeworkApp().run()
    # Get User and ID after login flow
    User = login.User
    ID = login.ID
    if result == "student":
        import student
        student.run_student_app(User, ID)
    elif result == "teacher":
        import teacher
        teacher.run_teacher_app(User, ID)
    else:
        import principal
        principal.run_principal_app(User, ID)