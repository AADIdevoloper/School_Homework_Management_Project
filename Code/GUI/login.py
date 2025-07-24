from textual.app import ComposeResult
from textual.widgets import Button, Label, Input, RadioSet, RadioButton
from textual.containers import Vertical
from textual.screen import Screen
from textual.reactive import var

# Global variables to be imported in main.py
User = None
ID = None

class WelcomeScreen(Screen):
    def compose(self) -> ComposeResult:
        """Composes the welcome screen with title, authors, and a proceed button."""
        yield Vertical(
            Label("Class XII Investigatory Project:\nHomework Management System\n", id="title"),
            Label("Developed by Shivam Gholap and Aadi Nigam\n ", id="authors"),
            Button("Proceed", id="proceed", variant="success"),
            id="welcome-container"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handles the proceed button to navigate to the login screen."""
        if event.button.id == "proceed":
            self.app.push_screen("login")

class LoginScreen(Screen):
    selected_role = var("Student")

    def compose(self) -> ComposeResult:
        """Composes the login screen with role selection and proceed button."""
        yield Vertical(
            Label("Login", id="login-title"),
            RadioSet(
                RadioButton("Principal", id="Principal"),
                RadioButton("Teacher", id="Teacher"),
                RadioButton("Student", id="Student", value=True),
                id="role-select"
            ),
            Button("Proceed", id="login-proceed", variant="primary"),
            id="login-container"
        )

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        """Updates the selected role when a radio button is changed."""
        self.selected_role = event.pressed.id

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handles the proceed button to move to ID input screen based on role."""
        if event.button.id == "login-proceed":
            self.app.role = self.selected_role
            self.app.push_screen("id")

class IDScreen(Screen):
    def compose(self) -> ComposeResult:
        """Composes the ID input screen based on the selected role."""
        note = ""
        if self.app.role == "Student":
            note = "Enter any number between 1 to 20"
        elif self.app.role == "Teacher":
            note = "Enter any number between 1 to 15"
        else:
            note = "ID for Principal is 0"

        yield Vertical(
            Label(f"Role selected: {self.app.role}"),
            Input(placeholder="Enter ID", id="id_input"),
            Label(note, id="id_note"),
            Button("Login", id="login-button", variant="primary"),
            id="id-container"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Processes the entered ID and sets global User and ID variables."""
        global User, ID
        id_text = self.query_one("#id_input", Input).value
        try:
            id_val = int(id_text)
        except ValueError:
            id_val = 0

        User = self.app.role
        if User == "Student":
            ID = 2000 + int(id_val)
            self.app.exit("student")
        elif User == "Teacher":
            ID = 5000 + int(id_val)
            self.app.exit("teacher")
        else:
            ID = 1000
            self.app.exit("principal")
