from exception import ExceptionPositiveIntValue


class DialogueWithTheUser:
    @staticmethod
    def send_message(text):
        print(text)

    @staticmethod
    def _get_patient_id_number_from_converted_text(patient_id_as_text):
        if not patient_id_as_text.isdigit():
            raise ExceptionPositiveIntValue('Ошибка. ID пациента должно быть числом (целым, положительным)')
        return int(patient_id_as_text)

    def get_patient_id(self):
        patient_id_as_text = input('Введите ID пациента: ')
        patient_id = self._get_patient_id_number_from_converted_text(patient_id_as_text=patient_id_as_text)
        return patient_id

    @staticmethod
    def get_entered_command_message_from_user():
        return input('Введите команду: ')

    @staticmethod
    def request_confirmation_for_patient_discharge():
        user_answer = input('Желаете этого клиента выписать? (да/нет): ')
        if user_answer == 'да':
            return True
        return False
