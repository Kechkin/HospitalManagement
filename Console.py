from functions import validate_patient_id_from_input


class Console:
    @staticmethod
    def send_message(text):
        print(text)

    @staticmethod
    def get_message_patient_id(patient_id):
        result = input(patient_id)
        return validate_patient_id_from_input(result)

    @staticmethod
    def get_message(text):
        return input(text)
