from UseCases import UseCases
from Hospital import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from functions import validate_patient_id


class TestValidatePatientId:
    service = Hospital()
    app = UseCases(service)

    def test_validate_patient_id(self):
        self.service._list_of_patients = [2, 1, 1, 3, 0]
        assert validate_patient_id(3, self.service._list_of_patients) is None
        assert validate_patient_id(patient_id=3, patients_list=self.service._list_of_patients) is None

    def test_validate_patient_out_of_range_min(self):
        self.service._list_of_patients = [2, 1, 1, 3, 0]
        assert validate_patient_id(-12, self.service._list_of_patients) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_validate_patient_out_of_range_max(self):
        self.service._list_of_patients = [2, 1, 1, 3, 0]
        assert (validate_patient_id(6, self.service._list_of_patients)
                == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

    def test_validate_empty_value(self):
        self.service._list_of_patients = [2, 1, 1, 3, 0]
        assert validate_patient_id(None, self.service._list_of_patients) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_validate_empty_text(self):
        self.service._list_of_patients = [2, 1, 1, 3, 0]
        assert validate_patient_id(TEXT, self.service._list_of_patients) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
