from constants import ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from exception import ExceptionPositiveIntValue


class DialogueWithTheUser:
    @staticmethod
    def send_message(text):
        print(text)

    @staticmethod
    def _get_converted_text_to_patient_id_value(patient_id_as_text):
        if not patient_id_as_text.isdigit():
            raise ExceptionPositiveIntValue(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
        return int(patient_id_as_text)

    def get_patient_id(self):
        patient_id_as_text = input('Введите ID пациента: ')
        patient_id = self._get_converted_text_to_patient_id_value(patient_id_as_text=patient_id_as_text)
        return patient_id

    @staticmethod
    def get_message():
        return input('Введите команду: ')

    @staticmethod
    def get_message_to_discharge_patient():
        return input('Желаете этого клиента выписать? (да/нет):')
