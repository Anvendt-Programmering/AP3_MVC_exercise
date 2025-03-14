from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import Controller

from Pyside6 import QWidgets

class View:
    def __init__(self):
        self.controller: "Controller"

    def set_controller(self, controller: "Controller"):
        self.controller = controller

    def show_message(self, message):
        print(message)

    def get_input(self):
        string_output = """----
Options:
1. Add Patient
2. Show patient list
3. Add Note
4. Print Anonymized patient note
5. Print patient note
0. Exit
----"""

        print(string_output)
        value = input("select option:")

        return value

    def add_patient(self):
        print("Adding Patient:")
        name = input(" name:")
        id = input(" Patient id:")
        dob = input(" date of birth:")
        return name, id, dob

    def input_patient_id(self):
        return input("Enter patient id:")

    def input_patient_note(self):
        return input("Enter patient note:")


class ViewPyside()