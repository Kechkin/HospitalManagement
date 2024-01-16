from exception import ExceptionNoPatientInHospital
from functions import generate_patients_with_statuses_from_zero_to_three


class Hospital:
    _list_of_patients = None

    def __init__(self, list_of_patients=None):
        if list_of_patients:
            self._list_of_patients = list_of_patients
        else:
            _list_of_patients = generate_patients_with_statuses_from_zero_to_three(200, 1)

    def check_if_patient_is_on_the_list(self, patient_id):
        if patient_id > self.get_count_of_patients():
            raise ExceptionNoPatientInHospital('Ошибка. В больнице нет пациента с таким ID')

    def get_count_of_patients(self):
        return len(self._list_of_patients)

    def discharge(self, patient_id: int):
        self.check_if_patient_is_on_the_list(patient_id=patient_id)
        self._list_of_patients.pop(patient_id - 1)

    def approve_to_decrease_status(self, patient_id: int):
        self.check_if_patient_is_on_the_list(patient_id=patient_id)
        if self._list_of_patients[patient_id - 1] == 0:
            return False
        return True

    def decrease_status(self, patient_id: int):
        self.check_if_patient_is_on_the_list(patient_id=patient_id)
        self.change_patient_status(patient_id=patient_id, status=-1)

    def approve_to_increase_of_status(self, patient_id: int):
        self.check_if_patient_is_on_the_list(patient_id=patient_id)
        if self._list_of_patients[patient_id - 1] == 3:
            return False
        return True

    def increase_status(self, patient_id: int):
        self.check_if_patient_is_on_the_list(patient_id=patient_id)
        self.change_patient_status(patient_id=patient_id, status=+1)

    def change_patient_status(self, patient_id, status):
        self._list_of_patients[patient_id - 1] += status

    def get_status_name_by_patient_id(self, patient_id: int):
        self.check_if_patient_is_on_the_list(patient_id=patient_id)
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
            'Тяжело болен': self._list_of_patients.count(0),
            'Болен': self._list_of_patients.count(1),
            'Слегка болен': self._list_of_patients.count(2),
            'Готов к выписке': self._list_of_patients.count(3),
        }
        return data_for_calculate_status
