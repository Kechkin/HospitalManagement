from HospitalApp import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from functions import generate_patients_with_statuses


class TestDischarge:
    app = Hospital()

    def test_len_of_patients_list(self):
        self.app._list_of_patients = [1, 1, 2, 3, 0, 1]
        self.app.discharge_patient(patient_id=3)
        assert self.app._list_of_patients == [1, 1, 3, 0, 1]

    def test_empty_list(self):
        self.app._list_of_patients = generate_patients_with_statuses(0, 2)
        assert self.app.discharge_patient(100) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def test_input_text(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        assert self.app.discharge_patient(TEXT) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_input_max_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        assert self.app.discharge_patient(13) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def test_input_min_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        assert self.app.discharge_patient(-11) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_empty_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        assert self.app.discharge_patient(None) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
