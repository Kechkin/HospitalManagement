from HospitalApp import Hospital
from functions import generate_patients_with_statuses


class TestProtectedMethods:
    app = Hospital()

    def test_get_new_patient_status(self):
        self.app._list_of_patients = generate_patients_with_statuses(10, 0)
        assert self.app._get_new_patient_status(8) == 'Новый статус пациента: Тяжело болен'

    def test_get_patient_by_id(self):
        self.app._list_of_patients = generate_patients_with_statuses(15, 0)
        assert self.app._get_patient_by_id(12) == 0
