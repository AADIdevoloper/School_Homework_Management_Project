from textual.app import App
from login import WelcomeScreen, LoginScreen, IDScreen, User, ID
from connection import connection, close_connection

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