from constants import PATIENT_DISCHARGED, ERROR_THERE_IS_NO_PATIENT_ID


class BaseLogic:
    def discharge(self, patient_id, list_of_patient):
        if list_of_patient and patient_id <= len(list_of_patient):
            list_of_patient.pop(patient_id - 1)
            return PATIENT_DISCHARGED
        else:
            return ERROR_THERE_IS_NO_PATIENT_ID
