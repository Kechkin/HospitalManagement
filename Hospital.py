from constants import ZERO, PATIENT_STATUSES, THREE, ERROR_DECREASE, PATIENT_READY_TO_DISCHARGE, YES, PATIENT_DISCHARGED, SESSION_END, \
    ERROR_THERE_IS_NO_PATIENT_ID
from functions import generate_patients, get_calculated_results, check_patient_id, get_input


class Status:
    @staticmethod
    def get_status_patient(status_id: int):
        return PATIENT_STATUSES.get(status_id)


class Patient:
    _list_of_patients: list = generate_patients()

    def _get_patient_by_id(self, patient_id: int):
        return self._list_of_patients[patient_id - 1]

    def _get_new_patient_status(self, patient_id):
        status_id = self._list_of_patients[patient_id - 1]
        patient_status = Status.get_status_patient(status_id)
        return f'Новый статус пациента: {patient_status}'

    @check_patient_id
    def get_status_patient(self, patient_id):
        status_id = self._get_patient_by_id(patient_id)
        patient_status = Status.get_status_patient(status_id)
        return f'Статус пациента: {patient_status}'

    def _input(self, answer: str, patient_id: int):
        if answer == YES:
            return self.discharge_patient(patient_id)
        else:
            return PATIENT_READY_TO_DISCHARGE

    @check_patient_id
    def increase_status_patient(self, patient_id):
        if self._list_of_patients[patient_id - 1] == THREE:
            answer = get_input('Желаете этого клиента выписать? (да/нет):')
            return self._input(answer, patient_id)
        self._list_of_patients[patient_id - 1] += 1
        return self._get_new_patient_status(patient_id)

    @check_patient_id
    def decrease_status_patient(self, patient_id):
        if self._list_of_patients[patient_id - 1] == ZERO:
            return ERROR_DECREASE
        self._list_of_patients[patient_id - 1] -= 1
        return self._get_new_patient_status(patient_id)

    @check_patient_id
    def discharge_patient(self, patient_id):
        if self._list_of_patients and patient_id <= len(self._list_of_patients):
            self._list_of_patients.pop(patient_id - 1)
            return PATIENT_DISCHARGED
        else:
            return ERROR_THERE_IS_NO_PATIENT_ID


class Hospital(Patient):
    def calculate_statistics(self):
        data = self._list_of_patients
        return get_calculated_results(data)

    def stop(self):
        return SESSION_END
