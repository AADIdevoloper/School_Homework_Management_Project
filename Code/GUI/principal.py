from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Input, DataTable, RadioSet, RadioButton
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.reactive import var
from connection import show_students, show_teachers, name, execute_query, fetch_all

Add = {}
Update = {}

class PrincipalHome(Screen):
    selected_option = var("edit")

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Hello Principal!"),
            RadioSet(
                RadioButton("View and Edit Teachers and Students", id="edit", value=True),
                RadioButton("View HW status with respect to Class", id="class"),
                RadioButton("View HW status with respect to Teacher", id="teacher"),
            ),
            Horizontal(
                Button("Proceed", id="proceed-btn", variant="primary"),
                Button("Exit", id="exit-btn", variant="error")
            )
        )

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        self.selected_option = event.pressed.id

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "exit-btn":
            self.app.exit()
        elif self.selected_option == "edit":
            self.app.push_screen(EditScreen())
        elif self.selected_option == "class":
            self.app.push_screen(ClassHWStatusScreen())
        else:
            self.app.push_screen(TeacherHWStatusScreen())

class EditScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("All Students"),
            DataTable(id="students-table"),
            Label("All Teachers"),
            DataTable(id="teachers-table"),
            Horizontal(
                Button("Add", id="add-btn", variant="success"),
                Button("Update", id="update-btn", variant="primary"),
                Button("Back", id="back-btn", variant="warning"),
            )
        )

    def on_mount(self) -> None:
        global students, teachers
        students = show_students()
        st_table = self.query_one("#students-table", DataTable)
        st_table.add_columns("ID", "Name", "DOB", "Class", "Completed HW", "Overall %", "Address")
        for student in students:
            st_table.add_row(student['id'], student['name'], student['DOB'], student['class'], student['completed_hw'], student['overall_percent'], student['address'])

        teachers = show_teachers()
        t_table = self.query_one("#teachers-table", DataTable)
        t_table.add_columns("ID", "Name", "Subject", "Class", "Assigned HW", "Overall %", "Address")
        for teacher in teachers:
            t_table.add_row(teacher['id'], teacher['name'], teacher['subject'], teacher['class'], teacher['assigned_hw'], teacher['overall_percent'], teacher['address'])

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-btn":
            self.app.push_screen(AddScreen())
        elif event.button.id == "update-btn":
            self.app.push_screen(UpdateScreen())
        else:
            self.app.pop_screen()

class AddScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Input(placeholder="ID", id="id"),
            Input(placeholder="Name", id="name"),
            Input(placeholder="DOB or Subject", id="special"),
            Input(placeholder="Class", id="class"),
            Input(placeholder="Address", id="address"),
            Horizontal(
                Button("Add", id="add-final", variant="success"),
                Button("Back", id="back", variant="warning")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        global Add
        if event.button.id == "add-final":
            Add = {
                "id": self.query_one("#id", Input).value,
                "name": self.query_one("#name", Input).value,
                "special": self.query_one("#special", Input).value,
                "class": self.query_one("#class", Input).value,
                "address": self.query_one("#address", Input).value,
            }
        self.app.pop_screen()

class UpdateScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Input(placeholder="ID", id="id"),
            Input(placeholder="Name", id="name"),
            Input(placeholder="DOB or Subject", id="special"),
            Input(placeholder="Class", id="class"),
            Input(placeholder="Address", id="address"),
            Horizontal(
                Button("Update", id="update-final", variant="primary"),
                Button("Back", id="back", variant="warning")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        global Update
        if event.button.id == "update-final":
            Update = {
                "id": self.query_one("#id", Input).value,
                "name": self.query_one("#name", Input).value,
                "special": self.query_one("#special", Input).value,
                "class": self.query_one("#class", Input).value,
                "address": self.query_one("#address", Input).value,
            }
        self.app.pop_screen()

class ClassHWStatusScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("HW Status - Class"),
            DataTable(id="class-table"),
            Button("Back", id="back-btn")
        )

    def on_mount(self) -> None:
        table = self.query_one("#class-table", DataTable)
        table.add_columns("Class", "Total HW", "Pending", "Percent Done")
        table.add_row("10", "15", "5", "66%")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

class TeacherHWStatusScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("HW Status - Teacher"),
            DataTable(id="teacher-table"),
            Button("Back", id="back-btn")
        )

    def on_mount(self) -> None:
        table = self.query_one("#teacher-table", DataTable)
        table.add_columns("Name", "Subject", "HWs Assigned", "Percent Completed")
        table.add_row("Mr. Verma", "Math", "6", "85%")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

class PrincipalApp(App):
    def __init__(self, user, ID):
        super().__init__()
        self.user = user
        self.ID = ID

    def on_mount(self) -> None:
        self.push_screen(PrincipalHome())

def run_principal_app(user, ID):
    app = PrincipalApp(user, ID)
    app.run()
