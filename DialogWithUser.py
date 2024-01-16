from exception import ExceptionPositiveIntValue


class DialogWithUser:
    _console = None

    def __init__(self, console=None):
        self._console = console

    def send_message(self, text):
        self._console.print(text)

    @staticmethod
    def _get_patient_id_number_from_converted_text(patient_id_as_text):
        if not patient_id_as_text.isdigit():
            raise ExceptionPositiveIntValue('Ошибка. ID пациента должно быть числом (целым, положительным)')
        return int(patient_id_as_text)

    def get_patient_id(self):
        patient_id_as_text = self._console.input('Введите ID пациента: ')
        patient_id = self._get_patient_id_number_from_converted_text(patient_id_as_text=patient_id_as_text)
        return patient_id

    def get_entered_command_message_from_user(self):
        return self._console.input('Введите команду: ')

    def request_confirmation_for_patient_discharge(self):
        user_answer = self._console.input('Желаете этого клиента выписать? (да/нет): ')
        if user_answer == 'да':
            return True
        return False
