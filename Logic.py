from constants import PATIENT_DISCHARGED


class BaseLogic:
    def discharge(self, patient_id, list_of_patient):
        list_of_patient.pop(patient_id - 1)
        return PATIENT_DISCHARGED

    def decrease_status(self, patient_id, list_of_patient):
        list_of_patient[patient_id - 1] -= 1
