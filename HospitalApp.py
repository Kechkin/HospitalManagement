from constants import (ZERO, PATIENT_STATUSES, THREE, ERROR_CANNOT_DECREASE_LOW_STATUS, \
                       PATIENT_STATUS_READY_TO_DISCHARGE, YES, PATIENT_DISCHARGED, SESSION_END,
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

    def _get_input(self, text):
        return input(text)

    def _validate_patient_id(self, patient_id):
        if not isinstance(patient_id, int) or patient_id <= ZERO:
            return ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
        elif patient_id > len(self.app.list_of_patients):
            return ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def get_status_patient(self, patient_id):
        result = self._validate_patient_id(patient_id)
        if not result:
            status_id = self.app.get_patient_by_id(patient_id=patient_id)
            patient_status = Status.get_status_patient(status_id)
            return f'Статус пациента: {patient_status}'
        else:
            return result

    def increase_status_patient(self, patient_id):
        result = self._validate_patient_id(patient_id)
        if not result:
            if self.app.get_patient_by_id(patient_id=patient_id) == THREE:
                answer = self._get_input('Желаете этого клиента выписать? (да/нет):')
                if answer == YES:
                    self.app.discharge(patient_id=patient_id)
                    return PATIENT_DISCHARGED
                else:
                    return PATIENT_STATUS_READY_TO_DISCHARGE
            self.app.increase(patient_id=patient_id)
            return self._get_new_patient_status(patient_id)
        else:
            return result

    def decrease_status_patient(self, patient_id):
        result = self._validate_patient_id(patient_id)
        if not result:
            if self.app.get_patient_by_id(patient_id=patient_id) == ZERO:
                return ERROR_CANNOT_DECREASE_LOW_STATUS
            self.app.decrease(patient_id=patient_id)
            return self._get_new_patient_status(patient_id)
        else:
            return result

    def discharge_patient(self, patient_id):
        result = self._validate_patient_id(patient_id)
        if not result:
            self.app.discharge(patient_id=patient_id)
            return PATIENT_DISCHARGED
        else:
            return result


class Hospital(Patient):
    def calculate_statistics(self):
        data = self.app.list_of_patients
        return get_calculated_results(data)

    def stop(self):
        return SESSION_END
