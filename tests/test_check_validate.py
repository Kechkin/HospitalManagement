from HospitalApp import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT


class TestValidatePatientId:
    app = Hospital()

    def test_validate_patient_id(self):
        self.app._list_of_patients = [2, 1, 1, 3, 0]
        assert self.app._validate_patient_id(3) is True
        assert self.app._validate_patient_id(patient_id=3) is True

    def test_validate_patient_out_of_range_min(self):
        self.app._list_of_patients = [2, 1, 1, 3, 0]
        assert self.app._validate_patient_id(-12) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_validate_patient_out_of_range_max(self):
        self.app._list_of_patients = [2, 1, 1, 3, 0]
        assert (self.app._validate_patient_id(6)
                == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

    def test_validate_empty_value(self):
        self.app._list_of_patients = [2, 1, 1, 3, 0]
        assert self.app._validate_patient_id(None) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_validate_empty_text(self):
        self.app._list_of_patients = [2, 1, 1, 3, 0]
        assert self.app._validate_patient_id(TEXT) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
