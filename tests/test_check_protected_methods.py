from HospitalApp import Hospital
from Service import BaseLogic
from functions import generate_patients_with_statuses


class TestProtectedMethods:
    service = BaseLogic()
    app = Hospital(service)

    def test_get_new_patient_status(self):
        self.service._list_of_patients = generate_patients_with_statuses(10, 0)
        assert self.app._get_new_patient_status(8) == 'Новый статус пациента: Тяжело болен'

    def test_get_patient_by_id(self):
        self.service._list_of_patients = generate_patients_with_statuses(15, 0)
        # assert self.app._get_patient_by_id(12) == 0
        assert self.service.get_patient_by_id(12) == 0
