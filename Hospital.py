from constants import ZERO, ERROR_CANNOT_DECREASE_LOW_STATUS, THREE, ONE, TWO
from functions import generate_patients_with_statuses_from_zero_to_three


class Hospital:
    _list_of_patients = generate_patients_with_statuses_from_zero_to_three(200, 1)

    def get_count_of_patients(self):
        return len(self._list_of_patients)

    def discharge(self, patient_id: int):
        self._list_of_patients.pop(patient_id - 1)

    def decrease(self, patient_id: int):
        if self._get_status_number_by_patient_id(patient_id=patient_id) == ZERO:
            return ERROR_CANNOT_DECREASE_LOW_STATUS
        else:
            self._list_of_patients[patient_id - 1] -= 1

    def increase(self, patient_id: int):
        if self._get_status_number_by_patient_id(patient_id=patient_id) == THREE:
            return True
        self._list_of_patients[patient_id - 1] += 1

    def _get_status_number_by_patient_id(self, patient_id: int):
        return self._list_of_patients[patient_id - 1]

    def get_status_name_by_patient_id(self, patient_id: int):
        patient_statuses: dict = {
            0: 'Тяжело болен',
            1: 'Болен',
            2: 'Слегка болен',
            3: 'Готов к выписке'
        }
        status_id = self._get_status_number_by_patient_id(patient_id=patient_id)
        new_patients_status = patient_statuses.get(status_id)
        return new_patients_status

    def get_calculated_statistics(self):
        data_for_calculate_status = {
            'Тяжело болен': self._list_of_patients.count(ZERO),
            'Болен': self._list_of_patients.count(ONE),
            'Слегка болен': self._list_of_patients.count(TWO),
            'Готов к выписке': self._list_of_patients.count(THREE),
        }
        return data_for_calculate_status