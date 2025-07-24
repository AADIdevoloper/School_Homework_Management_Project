from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Input, DataTable, RadioSet, RadioButton
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.reactive import var
from connection import pendinghw, update_homework_status, name, execute_query, fetch_all

# External input variable
completed_homework_srno = None

class StudentHome(Screen):
    selected_option = var("view")

    def compose(self) -> ComposeResult:
        """Composes the home screen with greeting and options."""
        yield Vertical(
            Label(f"Hello, {name(self.app.ID)}!", id="greeting"),
            RadioSet(
                RadioButton("View Pending Homework", id="view", value=True),
                RadioButton("Update Homework Status", id="update"),
                id="student-options"
            ),
            Horizontal(
                Button("Proceed", id="proceed-btn", variant="primary"),
                Button("Exit", id="exit-btn", variant="error"),
                id="button-row"
            ),
            id="student-home"
        )

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        """Updates the selected option when radio button changes."""
        self.selected_option = event.pressed.id

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Navigates to the selected option's screen or exits."""
        if event.button.id == "proceed-btn":
            if self.selected_option == "view":
                self.app.push_screen("view")
            else:
                self.app.push_screen("update")
        elif event.button.id == "exit-btn":
            self.app.exit()

class ViewHomeworkScreen(Screen):
    def compose(self) -> ComposeResult:
        """Displays student's pending homework in a table."""
        yield Vertical(
            Label(f"{name(self.app.ID)}", id="title"),
            DataTable(id="homework-table"),
            Button("Back", id="back-view"),
            id="view-container"
        )

    def on_mount(self) -> None:
        """Loads and populates pending homework data."""
        result = pendinghw(self.app.ID)
        if result:
            records = [(item['date'], item['subject'], item['title'], item['description'], item['due']) for item in result]
            table = self.query_one("#homework-table", DataTable)
            table.add_columns("Date", "Subject", "Title", "Description", "Due")
            for record in records:
                table.add_row(*record)
        else:
            table = self.query_one("#homework-table", DataTable)
            table.add_columns("No pending homework found")
            table.add_row("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Returns to the student home screen."""
        self.app.pop_screen()

class UpdateHomeworkScreen(Screen):
    def compose(self) -> ComposeResult:
        """Displays pending homework and input to update status."""
        yield Vertical(
            Label("Update Homework Status", id="update-title"),
            DataTable(id="pending-table"),
            Input(placeholder="Enter Sr. No. of completed homework", id="srno-input"),
            Button("Update", id="update-btn", variant="primary"),
            Button("Back", id="back-update", variant="warning"),
            id="update-container"
        )

    def on_mount(self) -> None:
        """Loads homework to update status for current week."""
        global result
        result = update_homework_status(id=self.app.ID, sr_no=completed_homework_srno)
        if result:
            records = [(item['sr_no'], item['date'], item['subject'], item['title'], item['due']) for item in result]
            table = self.query_one("#pending-table", DataTable)
            table.add_columns("Sr. No.", "Assigned on", "Subject", "Title", "Due")
            for record in records:
                table.add_row(*record)
        else:
            table = self.query_one("#pending-table", DataTable)
            table.add_columns("No pending homework found in this week")
            table.add_row("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Processes homework status update on user input."""
        global completed_homework_srno
        if event.button.id == "update-btn":
            completed_homework_srno = self.query_one("#srno-input", Input).value
            try:
                srno_int = int(completed_homework_srno)
            except ValueError:
                self.query_one("#update-title", Label).update("Please enter a valid Sr. No.")
                return
            updated = False
            for dict in result:
                if dict['sr_no'] == srno_int:
                    class_ = fetch_all(f"SELECT class FROM students WHERE id = {self.app.ID}")[0]['class']
                    query = f"UPDATE `{dict['date']}` SET id{self.app.ID} = 1 WHERE id{self.app.ID} = 0 AND class = '{class_}' AND title = '{dict['title']}' AND subject = '{dict['subject']}'"
                    execute_query(query)
                    self.query_one("#update-title", Label).update("Homework status updated successfully!")
                    updated = True
                    break
            if not updated:
                self.query_one("#update-title", Label).update("No matching homework found for the entered Sr. No.")
            self.set_timer(2, self.app.pop_screen)
        elif event.button.id == "back-update":
            self.app.pop_screen()

class StudentApp(App):
    CSS = """
    #student-home, #view-container, #update-container {
        align: center middle;
        height: 100%;
    }

    #greeting, #title, #update-title {
        text-align: center;
        margin-bottom: 1;
    }

    #success-msg {
        color: green;
        margin-top: 1;
    }

    #button-row {
        padding-top: 1;
        content-align: center middle;
    }

    #proceed-btn, #exit-btn {
        margin-left: 1;
        margin-right: 1;
    }"""

    def __init__(self, user, ID):
        """Initializes the StudentApp with user role and ID."""
        super().__init__()
        self.user = user
        self.ID = ID

    def on_mount(self) -> None:
        """Sets up and displays the student home screen."""
        self.install_screen(StudentHome(), name="home")
        self.install_screen(ViewHomeworkScreen(), name="view")
        self.install_screen(UpdateHomeworkScreen(), name="update")
        self.push_screen("home")

def run_student_app(user, ID):
    """Runs the student Textual app."""
    app = StudentApp(user, ID)
    app.run()
