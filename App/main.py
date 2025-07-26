from textual.app import App
from login import WelcomeScreen, LoginScreen, IDScreen, User, ID
from connection import connection, fetch_all, today, date_range, execute_query

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
        """Mounts the welcome, login, and ID screens on app start."""
        self.install_screen(WelcomeScreen(), name="welcome")
        self.install_screen(LoginScreen(), name="login")
        self.install_screen(IDScreen(), name="id")
        self.push_screen("welcome")

if __name__ == "__main__":

    # Ensure daily homework table exists for each student
    for date in date_range(today()):
        query="SELECT id FROM students"
        student_ids = [row['id'] for row in fetch_all(query)]

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
        execute_query(query)

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
