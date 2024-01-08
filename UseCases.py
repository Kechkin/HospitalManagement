from Console import Console
from constants import ZERO, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT, YES, \
    PATIENT_STATUS_READY_TO_DISCHARGE, PATIENT_DISCHARGED, ERROR_CANNOT_DECREASE_LOW_STATUS
from exception import ExceptionNoPatientInHospital, ExceptionPositiveIntValue


class UseCases:
    ent = None
    client_answer = None

    def __init__(self, entities):
        self.ent = entities

    @staticmethod
    def _validate_patient_id(patient_id: int):
        if not isinstance(patient_id, int) or patient_id < ZERO:
            raise ExceptionPositiveIntValue(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)

    def get_status_patient(self, patient_id: int):
        try:
            self._validate_patient_id(patient_id=patient_id)
            status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
            Console.send_message(f'Статус пациента: {status_name}')
        except (ExceptionNoPatientInHospital, ExceptionPositiveIntValue) as error:
            Console.send_message(error.args[0])

    def _ask_client_to_discharge_patient(self):
        self.client_answer = Console.get_message('Желаете этого клиента выписать? (да/нет):')
        if self.client_answer == YES:
            return True
        return False

    def increase_status_patient(self, patient_id: int):
        try:
            self._validate_patient_id(patient_id=patient_id)
            if self.ent.can_increase_status_patient_id(patient_id=patient_id) is False:
                if self._ask_client_to_discharge_patient():
                    self.ent.discharge(patient_id=patient_id)
                    Console.send_message(PATIENT_DISCHARGED)
                else:
                    Console.send_message(PATIENT_STATUS_READY_TO_DISCHARGE)
            else:
                self.ent.increase_status(patient_id=patient_id)
                status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
                Console.send_message(f'Новый статус пациента: {status_name}')
        except (ExceptionNoPatientInHospital, ExceptionPositiveIntValue) as error:
            Console.send_message(error.args[0])

    def decrease_status_patient(self, patient_id: int):
        try:
            self._validate_patient_id(patient_id=patient_id)
            if self.ent.can_decrease_status_patient_id(patient_id=patient_id) is False:
                Console.send_message(ERROR_CANNOT_DECREASE_LOW_STATUS)
            else:
                self.ent.decrease_status(patient_id=patient_id)
                status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
                Console.send_message(f'Новый статус пациента: {status_name}')
        except (ExceptionNoPatientInHospital, ExceptionPositiveIntValue) as error:
            Console.send_message(error.args[0])

    def discharge_patient(self, patient_id: int):
        try:
            self._validate_patient_id(patient_id=patient_id)
            self.ent.discharge(patient_id=patient_id)
            Console.send_message(PATIENT_DISCHARGED)
        except (ExceptionNoPatientInHospital, ExceptionPositiveIntValue) as error:
            Console.send_message(error.args[0])

    def show_calculated_hospital_statistics(self):
        calculated_statistics_data = self.ent.get_calculated_statistics()
        count_patients = self.ent.get_count_of_patients()
        result = f'В больнице на данный момент находится {count_patients} чел., из них: \n'
        for k, v in calculated_statistics_data.items():
            if v != ZERO:
                result += f'        в статусе "{k}": {v} чел. \n'
        Console.send_message(result)
