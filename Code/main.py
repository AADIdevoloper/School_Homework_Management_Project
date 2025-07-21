from connection import connection, close_connection, execute_query, fetch_all


import npyscreen

import npyscreen

class MainForm(npyscreen.Form):
    def create(self):
        # Store inputs as instance variables
        self.input1 = self.add(npyscreen.TitleText, name="Red Input:", color="DANGER")
        self.input2 = self.add(npyscreen.TitleText, name="Green Input:", color="GOOD")
        
        # Add button with callback to a method
        self.button = self.add(npyscreen.ButtonPress, name="Show Input", color="STANDOUT")
        self.button.whenPressed = self.on_button_press

    def on_button_press(self):
        # Access input box values
        val1 = self.input1.value
        val2 = self.input2.value
        npyscreen.notify_confirm(f"You entered:\nRed Input: {val1}\nGreen Input: {val2}", title="User Input")

class MyApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Input and Button Demo")

if __name__ == '__main__':
    MyApp().run()
