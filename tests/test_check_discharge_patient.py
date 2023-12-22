from HospitalApp import Hospital
from Service import BaseLogic
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from functions import generate_patients_with_statuses


class TestDischarge:
    service = BaseLogic()
    app = Hospital(service)

    def test_len_of_patients_list(self):
        self.service._list_of_patients = [1, 2, 1]
        self.app.discharge_patient(3)
        assert self.service._list_of_patients == [1, 2]

    def test_empty_list(self):
        assert self.app.discharge_patient(100) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def test_input_text(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        assert self.app.discharge_patient(TEXT) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_input_max_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        assert self.app.discharge_patient(300) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def test_input_min_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        assert self.app.discharge_patient(-11) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_empty_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        assert self.app.discharge_patient(None) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
