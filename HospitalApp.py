from constants import (ZERO, PATIENT_STATUSES, SESSION_END,
                       ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID,
                       ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
from functions import get_calculated_results


class Status:
    @staticmethod
    def get_status_patient(status_id: int):
        return PATIENT_STATUSES.get(status_id)


class Patient:
    app = None

    def __init__(self, service):
        self.app = service

    def _get_new_patient_status(self, patient_id):
        status_id = self.app.get_patient_by_id(patient_id=patient_id)
        patient_status = Status.get_status_patient(status_id)
        return f'Новый статус пациента: {patient_status}'

    def _validate_patient_id(self, patient_id):
        if not isinstance(patient_id, int) or patient_id <= ZERO:
            return ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
        elif patient_id > len(self.app.list_of_patients):
            return ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def get_status_patient(self, patient_id):
        validate_result = self._validate_patient_id(patient_id)
        if not validate_result:
            status_id = self.app.get_patient_by_id(patient_id=patient_id)
            patient_status = Status.get_status_patient(status_id)
            return f'Статус пациента: {patient_status}'
        else:
            return validate_result

    def increase_status_patient(self, patient_id):
        validate_result = self._validate_patient_id(patient_id)
        if not validate_result:
            increase_result = self.app.increase(patient_id=patient_id)
            if not increase_result:
                return self._get_new_patient_status(patient_id)
            return increase_result
        else:
            return validate_result

    def decrease_status_patient(self, patient_id):
        validate_result = self._validate_patient_id(patient_id)
        if not validate_result:
            decrease_result = self.app.decrease(patient_id=patient_id)
            if not decrease_result:
                return self._get_new_patient_status(patient_id)
            return decrease_result
        else:
            return validate_result

    def discharge_patient(self, patient_id):
        validate_result = self._validate_patient_id(patient_id)
        if not validate_result:
            return self.app.discharge(patient_id=patient_id)
        else:
            return validate_result


class Hospital(Patient):
    def calculate_statistics(self):
        data = self.app.list_of_patients
        return get_calculated_results(data)

    def stop(self):
        return SESSION_END
