from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller import Controller


class Patient:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__notes = []

    def add_note(self, note):
        self.__notes.append(note)

    def get_anonymized_patient_data(self):
        return_str = f"patient id:{self.__id}, dob:{self.__dob}"
        for s in self.__notes:
            return_str += f"\n  {s}"
        return return_str

    def get_patient_data(self):
        return_str = f"patient id:{self.__id}, name:{self.__name}, dob:{self.__dob}"
        for s in self.__notes:
            return_str += f"\n  {s}"
        return return_str

    def __str__(self):
        return self.get_anonymized_patient_data

    def __repr__(self):
        return self.get_anonymized_patient_data

    def get_id(self):
        return self.__id


class Model:
    def __init__(self):
        self.__patients: list[Patient] = []
        self.controller: "Controller"

    def set_controller(self, controller: "Controller"):
        self.controller = controller

    def add_patient(self, patient):
        for p in self.__patients:
            if p.get_id() == patient.get_id():
                return None
        self.__patients.append(patient)

    def add_note_to_patient(self, id, note):
        for patient in self.__patients:
            if patient.get_id() == id:
                patient.add_note(note)
                return patient
        return None

    def get_patient(self, id):
        for patient in self.__patients:
            if patient.get_id() == id:
                return patient
        return None

    def get_patient_ids(self):
        return [p.get_id() for p in self.__patients]
