from constants import ZERO, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT, ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, THREE, YES, \
    PATIENT_STATUS_READY_TO_DISCHARGE, PATIENT_DISCHARGED, ERROR_CANNOT_INCREASE_HIGH_STATUS
from exception import ExceptionNoPatientInHospital, ExceptionPositiveIntValue


class UseCases:
    ent = None
    client_answer = None

    def __init__(self, entities):
        self.ent = entities

    @staticmethod
    def _get_input(text):
        return input(text)

    def _validate_patient_id(self, patient_id):
        if not isinstance(patient_id, int) or patient_id < ZERO:
            raise ExceptionPositiveIntValue(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
        elif patient_id > self.ent.get_count_of_patients():
            raise ExceptionNoPatientInHospital(ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

    def get_status_patient(self, patient_id):
        try:
            self._validate_patient_id(patient_id=patient_id)
            status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
            return f'Статус пациента: {status_name}'
        except (ExceptionNoPatientInHospital, ExceptionPositiveIntValue) as error:
            return error.args[0]

    def increase_status_patient(self, patient_id):
        try:
            self._validate_patient_id(patient_id=patient_id)
            result = self.ent.increase(patient_id=patient_id)
            if result == ERROR_CANNOT_INCREASE_HIGH_STATUS:
                self.client_answer = self._get_input('Желаете этого клиента выписать? (да/нет):')
                if self.client_answer == YES:
                    self.ent.discharge(patient_id=patient_id)
                    return PATIENT_DISCHARGED
                return PATIENT_STATUS_READY_TO_DISCHARGE
            status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
            return f'Новый статус пациента: {status_name}'
        except (ExceptionNoPatientInHospital, ExceptionPositiveIntValue) as error:
            return error.args[0]

    def decrease_status_patient(self, patient_id):
        try:
            self._validate_patient_id(patient_id=patient_id)
            decrease_result = self.ent.decrease(patient_id=patient_id)
            if not decrease_result:
                status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
                return f'Новый статус пациента: {status_name}'
            return decrease_result
        except (ExceptionNoPatientInHospital, ExceptionPositiveIntValue) as error:
            return error.args[0]

    def discharge_patient_from_list(self, patient_id):
        try:
            self._validate_patient_id(patient_id=patient_id)
            self.ent.discharge(patient_id=patient_id)
            return PATIENT_DISCHARGED
        except (ExceptionNoPatientInHospital, ExceptionPositiveIntValue) as error:
            return error.args[0]

    def show_calculated_hospital_statistics(self):
        calculated_statistics_data = self.ent.get_calculated_statistics()
        count_patients = self.ent.get_count_of_patients()
        result = f'В больнице на данный момент находится {count_patients} чел., из них: \n'
        for k, v in calculated_statistics_data.items():
            if v != ZERO:
                result += f'        в статусе "{k}": {v} чел. \n'
        return result
