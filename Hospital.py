from constants import PATIENT_DISCHARGED, ZERO, ERROR_CANNOT_DECREASE_LOW_STATUS, YES, \
    THREE, PATIENT_STATUS_READY_TO_DISCHARGE, ONE, TWO, PATIENT_STATUSES, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from functions import generate_patients_with_statuses_from_zero_to_three


class Hospital:
    _list_of_patients = generate_patients_with_statuses_from_zero_to_three(200, 1)

    @property
    def list_of_patients(self):
        return self._list_of_patients

    @staticmethod
    def _get_input(text):
        return input(text)

    @staticmethod
    def _validate_patient_id_below_zero(patient_id):
        if patient_id <= ZERO:
            raise ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def discharge(self, patient_id: int):
        self._validate_patient_id_below_zero(patient_id=patient_id)
        self._list_of_patients.pop(patient_id - 1)
        return PATIENT_DISCHARGED

    def decrease(self, patient_id):
        self._validate_patient_id_below_zero(patient_id=patient_id)
        if self.get_status_number_by_patient_id(patient_id=patient_id) == ZERO:
            return ERROR_CANNOT_DECREASE_LOW_STATUS
        else:
            self.list_of_patients[patient_id - 1] -= 1

    def increase(self, patient_id):
        self._validate_patient_id_below_zero(patient_id=patient_id)
        if self.get_status_number_by_patient_id(patient_id=patient_id) == THREE:
            answer = self._get_input('Желаете этого клиента выписать? (да/нет):')
            if answer == YES:
                return self.discharge(patient_id=patient_id)
            return PATIENT_STATUS_READY_TO_DISCHARGE
        self.list_of_patients[patient_id - 1] += 1

    def get_status_number_by_patient_id(self, patient_id):
        return self._list_of_patients[patient_id - 1]

    def get_status_name_by_patient_id(self, patient_id):
        self._validate_patient_id_below_zero(patient_id=patient_id)
        status_id = self.get_status_number_by_patient_id(patient_id=patient_id)
        new_patients_status = PATIENT_STATUSES.get(status_id)
        return new_patients_status

    def get_calculated_statistics(self):
        data_for_calculate_status = {
            'Тяжело болен': self._list_of_patients.count(ZERO),
            'Болен': self._list_of_patients.count(ONE),
            'Слегка болен': self._list_of_patients.count(TWO),
            'Готов к выписке': self._list_of_patients.count(THREE),
        }
        return data_for_calculate_status
