from constants import ZERO, PATIENT_STATUSES, THREE
from workflow import generate_patients, show_calculated_results


class Status:
    @staticmethod
    def get_status_patient(status_id: int):
        return PATIENT_STATUSES.get(status_id)


class Patient:
    _list_of_patients: list = generate_patients()

    def _get_patient_by_id(self, patient_id: int):
        if patient_id > ZERO and isinstance(patient_id, int):
            return self._list_of_patients[patient_id - 1]

    def _get_new_patient_status(self, patient_id):
        status_id = self._list_of_patients[patient_id - 1]
        patient_status = Status.get_status_patient(status_id)
        return f'Новый статус пациента: {patient_status}'

    def get_status_patient(self, patient_id):
        status_id = self._get_patient_by_id(patient_id)
        patient_status = Status.get_status_patient(status_id)
        return f'Статус пациента: {patient_status}'

    def increase_status_patient(self, patient_id):
        if self._list_of_patients[patient_id - 1] == THREE:
            answer = input('Желаете этого клиента выписать? (да/нет):')
            if answer == 'да':
                return self.discharge_patient(patient_id)
            else:
                return 'Пациент остался в статусе "Готов к выписке"'
        self._list_of_patients[patient_id - 1] += 1
        return self._get_new_patient_status(patient_id)

    def decrease_status_patient(self, patient_id):
        if self._list_of_patients[patient_id - 1] == ZERO:
            return 'Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)'
        self._list_of_patients[patient_id - 1] -= 1
        return self._get_new_patient_status(patient_id)

    def discharge_patient(self, patient_id):
        self._list_of_patients.pop(patient_id - 1)
        return 'Пациент выписан из больницы'


class Hospital(Patient):
    def calculate_statistics(self):
        data = self._list_of_patients
        return show_calculated_results(data)

    def stop(self):
        return 'Сеанс завершён.'
