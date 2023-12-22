from constants import PATIENT_DISCHARGED, ERROR_THERE_IS_NO_PATIENT_ID
from functions import generate_patients_with_statuses


class BaseLogic:
    _list_of_patients = generate_patients_with_statuses(200, 1)

    def discharge(self, patient_id: int):
        self._list_of_patients.pop(patient_id - 1)

    def decrease(self, patient_id):
        self.list_of_patients[patient_id - 1] -= 1

    def increase(self, patient_id):
        self.list_of_patients[patient_id - 1] += 1

    def get_patient_by_id(self, patient_id):
        return self._list_of_patients[patient_id - 1]

    @property
    def list_of_patients(self):
        return self._list_of_patients
