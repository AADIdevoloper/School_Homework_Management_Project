import npyscreen

#Creds:
User='Not Selected'
ID=0

class WelcomeScreen(npyscreen.FormBaseNew):
    def create(self):
        max_y, max_x = self.useable_space()
        center_x = max_x // 2

        self.add(npyscreen.FixedText,
                 value="Hello World",
                 relx=center_x - len("Hello World") // 2,
                 rely=2,
                 color='STANDOUT')

        self.add(npyscreen.FixedText,
                 value="Developed by A and B",
                 relx=center_x - len("Developed by A and B") // 2,
                 rely=4,
                 color='LABEL')

        self.add(npyscreen.FixedText,
                 value="Note: This app is controlled via keyboard inputs ONLY",
                 relx=center_x - 25,
                 rely=6,
                 color='DANGER')

        self.proceed_btn = self.add(npyscreen.ButtonPress,
                                    name="Proceed",
                                    relx=center_x - len("Proceed") // 2,
                                    rely=8,
                                    color='GOOD')
        self.proceed_btn.whenPressed = self.go_to_login

    def go_to_login(self):
        self.parentApp.setNextForm("LOGIN")
        self.editing = False


class LoginScreen(npyscreen.FormBaseNew):
    def create(self):
        self.add(npyscreen.FixedText, value="Login", relx=2, rely=1, color='STANDOUT')

        self.role = self.add(npyscreen.TitleSelectOne,
                             name="Select your role:",
                             values=["Principal", "Teacher", "Student"],
                             max_height=5,
                             scroll_exit=True,
                             rely=3)

        self.proceed_btn = self.add(npyscreen.ButtonPress,
                                    name="Proceed",
                                    rely=9,
                                    relx=4,
                                    color='GOOD')
        self.proceed_btn.whenPressed = self.open_id_prompt

    def open_id_prompt(self):
        selected = self.role.get_selected_objects()
        if selected:
            self.parentApp.selected_role = selected[0]
            self.parentApp.setNextForm("IDFORM")
            self.editing = False


class IDPrompt(npyscreen.ActionForm):
    def create(self):
        self.id_input = self.add(npyscreen.TitleText, name="Enter ID:")
        self.note = self.add(npyscreen.FixedText, value="")

    def beforeEditing(self):
        role = self.parentApp.selected_role
        if role == "Student":
            self.note.value = "Enter any number between 1 to 20"
        elif role == "Teacher":
            self.note.value = "Enter any number between 1 to 15"
        elif role == "Principal":
            self.note.value = "Press 0"

    def on_ok(self):
        self.parentApp.user_id = self.id_input.value
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.setNextForm(None)


class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", WelcomeScreen, name="Welcome")
        self.addForm("LOGIN", LoginScreen, name="Login")
        self.addForm("IDFORM", IDPrompt, name="Enter ID")
        self.selected_role = None
        self.user_id = None


if __name__ == '__main__':
    MyApp().run()
    print()