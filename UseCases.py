from Status import Status
from constants import ZERO
from functions import validate_patient_id


class UseCases:
    ent = None

    def __init__(self, entities):
        self.ent = entities

    def _get_new_patient_status(self, patient_id):
        status_id = self.ent.get_patient_by_id(patient_id=patient_id)
        new_patients_status = Status.get_status_patient(status_id)
        return f'Новый статус пациента: {new_patients_status}'

    def get_status_patient(self, patient_id):
        validated_result_patient_id = validate_patient_id(patient_id, self.ent.list_of_patients)
        if not validated_result_patient_id:
            status_id = self.ent.get_patient_by_id(patient_id=patient_id)
            patient_status = Status.get_status_patient(status_id)
            return f'Статус пациента: {patient_status}'
        else:
            return validated_result_patient_id

    def increase_status_patient(self, patient_id):
        validated_result_patient_id = validate_patient_id(patient_id, self.ent.list_of_patients)
        if not validated_result_patient_id:
            increase_result = self.ent.increase(patient_id=patient_id)
            if not increase_result:
                return self._get_new_patient_status(patient_id)
            return increase_result
        else:
            return validated_result_patient_id

    def decrease_status_patient(self, patient_id):
        validated_result_patient_id = validate_patient_id(patient_id, self.ent.list_of_patients)
        if not validated_result_patient_id:
            decrease_result = self.ent.decrease(patient_id=patient_id)
            if not decrease_result:
                return self._get_new_patient_status(patient_id)
            return decrease_result
        else:
            return validated_result_patient_id

    def discharge_patient_from_list(self, patient_id):
        validated_result_patient_id = validate_patient_id(patient_id, self.ent.list_of_patients)
        if not validated_result_patient_id:
            return self.ent.discharge(patient_id=patient_id)
        else:
            return validated_result_patient_id

    def show_calculated_hospital_statistics(self):
        calculated_statistics_data = self.ent.get_calculated_statistics()
        result = f'В больнице на данный момент находится {len(self.ent.list_of_patients)} чел., из них: \n'
        for k, v in calculated_statistics_data.items():
            if v != ZERO:
                result += f'        в статусе "{k}": {v} чел. \n'
        return result
