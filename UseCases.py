from constants import ZERO, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT, ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID


class UseCases:
    ent = None

    def __init__(self, entities):
        self.ent = entities

    def _get_new_patient_status(self, patient_id):
        status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
        return f'Новый статус пациента: {status_name}'

    def get_status_patient(self, patient_id):
        try:
            status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
            return f'Статус пациента: {status_name}'
        except TypeError:
            return ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
        except IndexError:
            return ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def increase_status_patient(self, patient_id):
        try:
            increase_result = self.ent.increase(patient_id=patient_id)
            if not increase_result:
                return self._get_new_patient_status(patient_id=patient_id)
        except TypeError:
            return ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
        except IndexError:
            return ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
        else:
            return increase_result

    def decrease_status_patient(self, patient_id):
        try:
            decrease_result = self.ent.decrease(patient_id=patient_id)
            if not decrease_result:
                return self._get_new_patient_status(patient_id=patient_id)
        except TypeError:
            return ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
        except IndexError:
            return ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
        else:
            return decrease_result

    def discharge_patient_from_list(self, patient_id):
        try:
            return self.ent.discharge(patient_id=patient_id)
        except TypeError:
            return ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
        except IndexError:
            return ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def show_calculated_hospital_statistics(self):
        calculated_statistics_data = self.ent.get_calculated_statistics()
        result = f'В больнице на данный момент находится {len(self.ent.list_of_patients)} чел., из них: \n'
        for k, v in calculated_statistics_data.items():
            if v != ZERO:
                result += f'        в статусе "{k}": {v} чел. \n'
        return result
