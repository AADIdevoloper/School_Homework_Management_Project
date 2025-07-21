from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Input, DataTable, RadioSet, RadioButton
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.reactive import var
from connection import add_homework, name, fetch_all

Add = {}
Update = {}

class TeacherHome(Screen):
    selected_option = var("view_edit")

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label(f"Hello {name(self.app.ID)}!", id="teacher-label"),
            RadioSet(
                RadioButton("View or edit homeworks", id="view_edit", value=True),
                RadioButton("View class HW status", id="class_status"),
                RadioButton("View individual student HW status", id="student_status"),
                id="teacher-options"
            ),
            Horizontal(
                Button("Proceed", id="proceed", variant="primary"),
                Button("Exit", id="exit", variant="error")
            ),
            id="teacher-home"
        )

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        self.selected_option = event.pressed.id

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "proceed":
            self.app.push_screen(self.selected_option)
        elif event.button.id == "exit":
            self.app.exit()

class ViewEditScreen(Screen):
    mode = var("")

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label(f'All {fetch_all(f"SELECT subject FROM teachers WHERE id = {self.app.ID}")[0]["subject"]} homeworks', id="subject-label"),
            DataTable(id="hw-table"),
            Horizontal(
                Button("Add", id="add-btn"),
                Button("Update", id="update-btn"),
                Button("Back", id="back-btn"),
                id="btn-row"
            ),
            id="view-edit-container"
        )

    def on_mount(self) -> None:
        table = self.query_one("#hw-table", DataTable)
        table.add_columns("Sr no.", "Date", "Title", "Class", "Description", "Assigned by", "Due")
        dummy_data = [
            ("1", "2025-07-01", "Map Work", "10A", "Draw India's map", "teacher1", "2025-07-20"),
            ("2", "2025-07-02", "Climate", "10B", "Complete exercise 3", "teacher1", "2025-07-21")
        ]
        for row in dummy_data:
            table.add_row(*row)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-btn":
            self.app.push_screen("add_hw")
        elif event.button.id == "update-btn":
            self.app.push_screen("update_hw")
        elif event.button.id == "back-btn":
            self.app.pop_screen()
class AddHomeworkScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Add Homework", id="add-label"),
            Input(placeholder="Title", id="add-title"),
            Input(placeholder="Class", id="add-class"),
            Input(placeholder="Description", id="add-desc"),
            Input(placeholder="Due Date", id="add-due"),
            Horizontal(
                Button("Add", id="submit-add", variant="success"),
                Button("Back", id="back-add", variant="primary")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        global Add
        if event.button.id == "submit-add":
            Add = {
                "title": self.query_one("#add-title", Input).value,
                "class": self.query_one("#add-class", Input).value,
                "description": self.query_one("#add-desc", Input).value,
                "due": self.query_one("#add-due", Input).value
            }
            add_homework(date='2023-10-02', teacher_id=self.app.ID, title=Add['title'], class_=Add['class'], description=Add['description'], due=Add['due'])
            self.query_one("#add-label", Label).update("Homework added successfully!")
            self.app.pop_screen()
        elif event.button.id == "back-add":
            self.app.pop_screen()

class UpdateHomeworkScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Update Homework", id="update-label"),
            Input(placeholder="Sr no.", id="upd-sr"),
            Input(placeholder="Title", id="upd-title"),
            Input(placeholder="Class", id="upd-class"),
            Input(placeholder="Description", id="upd-desc"),
            Input(placeholder="Due Date", id="upd-due"),
            Horizontal(
                Button("Update", id="submit-update", variant="success"),
                Button("Back", id="back-update", variant="primary")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        global Update
        if event.button.id == "submit-update":
            Update = {
                "sr_no": self.query_one("#upd-sr", Input).value,
                "title": self.query_one("#upd-title", Input).value,
                "class": self.query_one("#upd-class", Input).value,
                "description": self.query_one("#upd-desc", Input).value,
                "due": self.query_one("#upd-due", Input).value
            }
            self.app.pop_screen()
        elif event.button.id == "back-update":
            self.app.pop_screen()

class ClassStatusScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Class Homework Status", id="class-status-label"),
            DataTable(id="class-table"),
            Button("Back", id="back-class")
        )

    def on_mount(self) -> None:
        table = self.query_one("#class-table", DataTable)
        table.add_columns("Class", "Total Students", "No. of Submissions", "Percent Completed")
        data = [
            ("10A", "30", "27", "90%"),
            ("10B", "32", "29", "91%")
        ]
        for row in data:
            table.add_row(*row)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

class StudentStatusInputScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Individual Student HW Status", id="student-input-label"),
            Input(placeholder="Enter student name", id="student-name"),
            Input(placeholder="Enter class", id="student-class"),
            Horizontal(
                Button("Show", id="show-status", variant="success"),
                Button("Back", id="back-student-input", variant="primary")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "show-status":
            self.app.push_screen("student-status-table")
        elif event.button.id == "back-student-input":
            self.app.pop_screen()

class StudentStatusTableScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Homework Status for student_name", id="student-table-label"),
            DataTable(id="student-table"),
            Label("Total homework: 5   Homework due: 1   Percent done: 80%", id="summary"),
            Button("Back", id="back-student-table")
        )

    def on_mount(self) -> None:
        table = self.query_one("#student-table", DataTable)
        table.add_columns("Title", "Date", "Due", "Status")
        data = [
            ("Map Work", "2025-07-01", "2025-07-20", "Completed"),
            ("Climate", "2025-07-02", "2025-07-21", "Due")
        ]
        for row in data:
            table.add_row(*row)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

class TeacherApp(App):
    CSS = """
    #teacher-home, #view-edit-container {
        align: center middle;
        height: 100%;
    }
    #btn-row {
        padding-top: 1;
    }
    """
    def __init__(self, user, ID):
        super().__init__()
        self.user = user
        self.ID = ID

    def on_mount(self) -> None:
        self.install_screen(TeacherHome(), name="home")
        self.install_screen(ViewEditScreen(), name="view_edit")
        self.install_screen(AddHomeworkScreen(), name="add_hw")
        self.install_screen(UpdateHomeworkScreen(), name="update_hw")
        self.install_screen(ClassStatusScreen(), name="class_status")
        self.install_screen(StudentStatusInputScreen(), name="student_status")
        self.install_screen(StudentStatusTableScreen(), name="student-status-table")
        self.push_screen("home")

def run_teacher_app(user, ID):
    app = TeacherApp(user, ID)
    app.run()
