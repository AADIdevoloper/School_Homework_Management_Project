from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Input, DataTable, RadioSet, RadioButton
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.reactive import var
from connection import all_class_status, show_students, show_teachers, name, execute_query, fetch_all, add_student, add_teacher, update_student, update_teacher, all_teacher_status

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
                Button("Delete", id="delete-btn", variant="error"),
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
        elif event.button.id == "delete-btn":
            self.app.push_screen(DeleteScreen())
        else:
            self.app.pop_screen()

class AddScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Add Student or Teacher"),
            Label("ID should start with 2 for Student and 5 for Teacher",id="error-message"),
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
        if str(Add['id']).startswith("5"):
            add_teacher(Add['id'], Add['name'], Add['special'], Add['class'], Add['address'])
        elif str(Add['id']).startswith("2"):
            add_student(Add['id'], Add['name'], Add['special'], Add['class'], Add['address'])
        elif Add['id'] in [str(student['id']) for student in show_students()] + [str(teacher['id']) for teacher in show_teachers()]:
            self.query_one("#error-message", Label).update("The ID Already Exists! Use Update Button instead.")
        else:
            self.query_one("#error-message", Label).update("Invalid ID: ID should start with 2 for Student and 5 for Teacher")
        self.app.pop_screen()

class UpdateScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Update Student or Teacher"),
            Label("ID should start with 2 for Student and 5 for Teacher", id="error-message"),
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
            try:
                if str(Update['id']).startswith("5"):
                    update_teacher(Update['id'], Update['name'], Update['special'], Update['class'], Update['address'])
                elif str(Update['id']).startswith("2"):
                    update_student(Update['id'], Update['name'], Update['special'], Update['class'], Update['address'])
            except Exception as e:
                self.query_one("#error-message", Label).update("Error updating record, please try again")
        self.app.pop_screen()

class DeleteScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Delete Student or Teacher"),
            Label("ID should start with 2 for Student and 5 for Teacher", id="error-message"),
            Input(placeholder="ID", id="id"),
            Horizontal(
                Button("Delete", id="delete-final", variant="error"),
                Button("Back", id="back", variant="warning")
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "delete-final":
            id_to_delete = self.query_one("#id", Input).value
            if str(id_to_delete).startswith("5"):
                execute_query(f"DELETE FROM teachers WHERE id = {id_to_delete}")
            elif str(id_to_delete).startswith("2"):
                execute_query(f"DELETE FROM students WHERE id = {id_to_delete}")
            else:
                self.query_one("#error-message", Label).update("Invalid ID: ID should start with 2 for Student and 5 for Teacher")
        self.app.pop_screen()
class ClassHWStatusScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("HW Status - Class"),
            DataTable(id="class-table"),
            Button("Back", id="back-btn")
        )

    def on_mount(self) -> None:
        class_status = all_class_status()
        if class_status:
            records = [(item['class'], item['total_students'], item['no_of_submissions'], item['percent_completed']) for item in class_status]
            table = self.query_one("#class-table", DataTable)
            table.add_columns("Class", "Total Students", "Submissions", "Percent Done")
            for status in records:
                table.add_row(*status)
        else:
            table = self.query_one("#class-table", DataTable)
            table.add_columns("No class status found")
            table.add_row("")
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
        teacher_status = all_teacher_status()
        if teacher_status:
            records = [(item['name'], item['total_hw'], item['percent_completed']) for item in teacher_status]
            table = self.query_one("#teacher-table", DataTable)
            table.add_columns("Name", "Total HW Assigned", "Percent Completed by Students")
            for status in records:
                table.add_row(*status)
        else:
            table = self.query_one("#teacher-table", DataTable)
            table.add_columns("No teacher status found")
            table.add_row("")

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
