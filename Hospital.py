from constants import ZERO, THREE, ONE, TWO, ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
from exception import ExceptionNoPatientInHospital
from functions import generate_patients_with_statuses_from_zero_to_three


class Hospital:
    _list_of_patients = generate_patients_with_statuses_from_zero_to_three(200, 1)

    def _validate_exists_patient_id(self, patient_id):
        if patient_id > self.get_count_of_patients():
            raise ExceptionNoPatientInHospital(ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

    def get_count_of_patients(self):
        return len(self._list_of_patients)

    def discharge(self, patient_id: int):
        self._validate_exists_patient_id(patient_id=patient_id)
        self.discharge_patient_from_list(patient_id=patient_id)

    def discharge_patient_from_list(self, patient_id):
        self._list_of_patients.pop(patient_id - 1)

    def can_decrease_status_patient_id(self, patient_id: int):
        self._validate_exists_patient_id(patient_id=patient_id)
        return self.can_not_change_status(patient_id=patient_id, value=ZERO)

    def decrease_status(self, patient_id: int):
        self._validate_exists_patient_id(patient_id=patient_id)
        self.change_status_patient_id(patient_id=patient_id, value=-1)

    def can_increase_status_patient_id(self, patient_id: int):
        self._validate_exists_patient_id(patient_id=patient_id)
        return self.can_not_change_status(patient_id=patient_id, value=THREE)

    def can_not_change_status(self, patient_id, value):
        if self._list_of_patients[patient_id - 1] == value:
            return False

    def increase_status(self, patient_id: int):
        self._validate_exists_patient_id(patient_id=patient_id)
        self.change_status_patient_id(patient_id=patient_id, value=+1)

    def change_status_patient_id(self, patient_id, value):
        self._list_of_patients[patient_id - 1] += value

    def get_status_name_by_patient_id(self, patient_id: int):
        self._validate_exists_patient_id(patient_id=patient_id)
        patient_statuses: dict = {
            0: 'Тяжело болен',
            1: 'Болен',
            2: 'Слегка болен',
            3: 'Готов к выписке'
        }
        status_id = self._list_of_patients[patient_id - 1]
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
