from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Input, DataTable, RadioSet, RadioButton
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.reactive import var
from connection import add_homework, name, fetch_all, show_homework, execute_query, class_homework_status, individual_homework_status, today

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
                Button("Add", id="add-btn", variant="success"),
                Button("Update", id="update-btn", variant="primary"),
                Button("Delete", id="delete-btn",variant="error"),
                Button("Back", id="back-btn",variant="warning"),
                id="btn-row"
            ),
            id="view-edit-container"
        )

    def on_mount(self) -> None:
        global view
        view = show_homework(self.app.ID)
        if view:
            records = [(item['index'], item['date'], item['title'], item['class'], item['description'], item['due'], name(item['teacher_id'])) for item in view]
            table = self.query_one("#hw-table", DataTable)
            table.add_columns("Sr. No.","Date", "Title", "Class", "Description", "Due", "Assigned by")
            for record in records:
                table.add_row(*record)
        else:
            table = self.query_one("#hw-table", DataTable)
            table.add_columns("No homework found")
            table.add_row("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-btn":
            self.app.push_screen("add_hw")
        elif event.button.id == "update-btn":
            self.app.push_screen("update_hw")
        elif event.button.id == "delete-btn":
            self.app.push_screen("delete_hw")
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
            add_homework(date=today(), teacher_id=self.app.ID, title=Add['title'], class_=Add['class'], description=Add['description'], due=Add['due'])
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
        global result
        result = show_homework(self.app.ID)
        if event.button.id == "submit-update":
            Update = {
                "sr_no": self.query_one("#upd-sr", Input).value,
                "title": self.query_one("#upd-title", Input).value,
                "class": self.query_one("#upd-class", Input).value,
                "description": self.query_one("#upd-desc", Input).value,
                "due": self.query_one("#upd-due", Input).value
            }
            try:
                srno_int = int(Update['sr_no'])
            except ValueError:
                self.query_one("#update-label", Label).update("Please enter a valid Sr. No.")
                return
            updated = False
            for dict in result:
                if dict['index'] == srno_int:
                    query = f"""UPDATE `{dict['date']}` SET title = \"{Update['title'] if Update['title'] else dict['title']}\",
                    class = \"{Update['class'] if Update['class'] else dict['class']}\",
                    description = \"{Update['description'] if Update['description'] else dict['description']}\",
                    due = \"{Update['due'] if Update['due'] else dict['due']}\" WHERE sr_no = {dict['sr_no']} AND teacher_id = {self.app.ID}"""
                    execute_query(query)
                    self.query_one("#update-label", Label).update("Homework status updated successfully!")
                    updated = True
                    break
            if not updated:
                self.query_one("#update-label", Label).update("No matching homework found for the entered Sr. No.")
            self.set_timer(2, self.app.pop_screen)
        elif event.button.id == "back-update":
            self.app.pop_screen()

class DeleteHomeworkScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Delete Homework", id="delete-label"),
            Input(placeholder="Sr no.", id="del-sr"),
            Horizontal(
                Button("Delete", id="submit-delete", variant="error"),
                Button("Back", id="back-delete", variant="primary")
            ))
    def on_button_pressed(self, event: Button.Pressed) -> None:
        global result
        result = show_homework(self.app.ID)
        if event.button.id == "submit-delete":
            sr_no = self.query_one("#del-sr", Input).value
            try:
                sr_no_int = int(sr_no)
            except ValueError:
                self.query_one("#delete-label", Label).update("Please enter a valid Sr. No.")
                return
            deleted = False
            for dict in result:
                if dict['index'] == sr_no_int:
                    query = f"DELETE FROM `{dict['date']}` WHERE sr_no = {dict['sr_no']} AND teacher_id = {self.app.ID}"
                    execute_query(query)
                    self.query_one("#delete-label", Label).update("Homework deleted successfully!")
                    deleted = True
                    break
            if not deleted:
                self.query_one("#delete-label", Label).update("No matching homework found for the entered Sr. No.")
            self.set_timer(2, self.app.pop_screen)
        elif event.button.id == "back-delete":
            self.app.pop_screen()
class ClassStatusScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Class Homework Status", id="class-status-label"),
            DataTable(id="class-table"),
            Button("Back", id="back-class")
        )

    def on_mount(self) -> None:
        class_status = class_homework_status(self.app.ID)
        if class_status:
            records = [(item['class'], item['total_students'], item['no_of_submissions'], item['percent_completed']) for item in class_status]
            table = self.query_one("#class-table", DataTable)
            table.add_columns("Class", "Total Students", "No. of Submissions", "Percent Completed")
            for record in records:
                table.add_row(*record)
        else:
            table = self.query_one("#class-table", DataTable)
            table.add_columns("No homework found")
            table.add_row("")

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
        global result
        result = individual_homework_status(name=self.query_one("#student-name", Input).value, class_=self.query_one("#student-class", Input).value)
        if event.button.id == "show-status":
            self.app.push_screen("student-status-table")
        elif event.button.id == "back-student-input":
            self.app.pop_screen()

class StudentStatusTableScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Homework Status for student_name", id="student-table-label"),
            DataTable(id="student-table"),
            Button("Back", id="back-student-table")
        )

    def on_mount(self) -> None:
        global result
        if not result:
            self.query_one("#student-table-label", Label).update("No homework found for the specified student. \nPlease check the name and class.")
            self.app.pop_screen()
        else:
            records = [(item['title'], item['date'], item['due'], item['status']) for item in result]
            table = self.query_one("#student-table", DataTable)
            table.add_columns("Title", "Date", "Due", "Status")
            for record in records:
                table.add_row(*record)

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
        self.install_screen(DeleteHomeworkScreen(), name="delete_hw")
        self.install_screen(ClassStatusScreen(), name="class_status")
        self.install_screen(StudentStatusInputScreen(), name="student_status")
        self.install_screen(StudentStatusTableScreen(), name="student-status-table")
        self.push_screen("home")

def run_teacher_app(user, ID):
    app = TeacherApp(user, ID)
    app.run()
