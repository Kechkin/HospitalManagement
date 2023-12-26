from constants import ZERO, PATIENT_STATUSES
from functions import validate_patient_id


class Status:
    @staticmethod
    def get_status_patient(status_id: int):
        return PATIENT_STATUSES.get(status_id)


class UseCases:
    app = None

    def __init__(self, hospital):
        self.app = hospital

    def _get_new_patient_status(self, patient_id):
        status_id = self.app.get_patient_by_id(patient_id=patient_id)
        patient_status = Status.get_status_patient(status_id)
        return f'Новый статус пациента: {patient_status}'

    def get_status_patient(self, patient_id):
        validate_result = validate_patient_id(patient_id, self.app.list_of_patients)
        if not validate_result:
            status_id = self.app.get_patient_by_id(patient_id=patient_id)
            patient_status = Status.get_status_patient(status_id)
            return f'Статус пациента: {patient_status}'
        else:
            return validate_result

    def increase_status_patient(self, patient_id):
        validate_result = validate_patient_id(patient_id, self.app.list_of_patients)
        if not validate_result:
            increase_result = self.app.increase(patient_id=patient_id)
            if not increase_result:
                return self._get_new_patient_status(patient_id)
            return increase_result
        else:
            return validate_result

    def decrease_status_patient(self, patient_id):
        validate_result = validate_patient_id(patient_id, self.app.list_of_patients)
        if not validate_result:
            decrease_result = self.app.decrease(patient_id=patient_id)
            if not decrease_result:
                return self._get_new_patient_status(patient_id)
            return decrease_result
        else:
            return validate_result

    def discharge_patient(self, patient_id):
        validate_result = validate_patient_id(patient_id, self.app.list_of_patients)
        if not validate_result:
            return self.app.discharge(patient_id=patient_id)
        else:
            return validate_result

    def show_calculated_statistics(self):
        calculated_data = self.app.get_calculated_results()
        result = f'В больнице на данный момент находится {len(self.app.list_of_patients)} чел., из них: \n'
        for k, v in calculated_data.items():
            if v != ZERO:
                result += f'        в статусе "{k}": {v} чел. \n'
        return result
