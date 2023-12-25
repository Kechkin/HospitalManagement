from constants import PATIENT_DISCHARGED, ZERO, ERROR_CANNOT_DECREASE_LOW_STATUS, YES, \
    THREE, PATIENT_STATUS_READY_TO_DISCHARGE
from functions import generate_patients_with_statuses


class BaseLogic:
    _list_of_patients = generate_patients_with_statuses(200, 1)

    def discharge(self, patient_id: int):
        self._list_of_patients.pop(patient_id - 1)
        return PATIENT_DISCHARGED

    def decrease(self, patient_id):
        if self.get_patient_by_id(patient_id=patient_id) == ZERO:
            return ERROR_CANNOT_DECREASE_LOW_STATUS
        else:
            self.list_of_patients[patient_id - 1] -= 1

    def _get_input(self, text):
        return input(text)

    def increase(self, patient_id):
        if self.get_patient_by_id(patient_id=patient_id) == THREE:
            answer = self._get_input('Желаете этого клиента выписать? (да/нет):')
            if answer == YES:
                return self.discharge(patient_id=patient_id)
            return PATIENT_STATUS_READY_TO_DISCHARGE
        self.list_of_patients[patient_id - 1] += 1

    def get_patient_by_id(self, patient_id):
        return self._list_of_patients[patient_id - 1]

    @property
    def list_of_patients(self):
        return self._list_of_patients
