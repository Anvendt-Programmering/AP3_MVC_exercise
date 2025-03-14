from models import Model, Patient
from views import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.__model = model
        self.__view = view

    def update(self):
        user_input = self.__view.get_input()

        """
        1. Add Patient
        2. Show patient list
        3. Add Note
        4. Print Anonymized patient note
        5. Print patient note
        0. Exit
        """

        match user_input:
            case "1":
                self.__add_patient()
            case "2":
                self.__show_patient_list()
            case "3":
                self.__add_note()
            case "4":
                self.__print_anonymized_patients_note()
            case "5":
                self.__print_patients_note()
            case "0":
                # Exit
                self.__view.show_message("Goodbye!")
            case _:
                self.__view.show_message("Invalid input. Please try again.")

        return user_input

    def __add_patient(self):
        name, id, dob = self.__view.add_patient()
        patient = Patient(name, id, dob)
        patient = self.__model.add_patient(patient)
        if patient is None:
            self.__view.show_message("Patient already exists.")
        else:
            self.__view.show_message("Patient Added.")

    def __show_patient_list(self):
        ids = self.__model.get_patient_ids()
        if ids:
            self.__view.show_message(f"Patient IDs: {ids}")
        else:
            self.__view.show_message("No patients found.")

    def __add_note(self):
        id = self.__view.input_patient_id()
        patient = self.__model.get_patient(id)
        if patient is None:
            self.__view.show_message("Patient not found.")
        else:
            note = self.__view.input_patient_note()
            patient.add_note(note)

    def __print_anonymized_patients_note(self):
        ids = self.__model.get_patient_ids()
        self.__view.show_message("----")
        if ids:
            self.__view.show_message("Patient IDs:")
        else:
            self.__view.show_message("No patients found.")

        for id in ids:
            patient = self.__model.get_patient(id)
            self.__view.show_message(patient.get_anonymized_patient_data())
            self.__view.show_message("----")

    def __print_patients_note(self):
        ids = self.__model.get_patient_ids()
        self.__view.show_message("----")
        if ids:
            self.__view.show_message("Patient IDs:")
        else:
            self.__view.show_message("No patients found.")

        for id in ids:
            patient = self.__model.get_patient(id)
            self.__view.show_message(patient.get_patient_data())
            self.__view.show_message("----")
