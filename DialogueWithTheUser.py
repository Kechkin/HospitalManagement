from constants import ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from exception import ExceptionPositiveIntValue


class Console:
    @staticmethod
    def send_message(text):
        print(text)

    @staticmethod
    def get_message_patient_id(patient_id):
        result = input(patient_id)
        # return validate_patient_id_from_input(result)

    # отв. с пользователем

    @staticmethod
    def _get_validate_patient_id(text):
        if not text.isdigit():
            raise ExceptionPositiveIntValue(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
        return int(text)

    def get_patient_id(self):
        patient_id_as_text = input('Введите ID пациента: ')
        patient_id = self._get_validate_patient_id(text=patient_id_as_text)
        return patient_id

    @staticmethod
    def get_message(text):
        return input(text)
