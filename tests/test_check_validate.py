from UseCases import UseCases
from Hospital import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from functions import validate_patient_id


class TestValidatePatientId:
    entities = Hospital()
    app = UseCases(entities)

    def test_validate_patient_id(self):
        self.entities._list_of_patients = [2, 1, 1, 3, 0]
        assert validate_patient_id(3, self.entities._list_of_patients) is None
        assert validate_patient_id(patient_id=3, patients_list=self.entities._list_of_patients) is None

    def test_validate_patient_out_of_range_min(self):
        self.entities._list_of_patients = [2, 1, 1, 3, 0]
        assert validate_patient_id(-12, self.entities._list_of_patients) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_validate_patient_out_of_range_max(self):
        self.entities._list_of_patients = [2, 1, 1, 3, 0]
        assert (validate_patient_id(6, self.entities._list_of_patients)
                == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

    def test_validate_empty_value(self):
        self.entities._list_of_patients = [2, 1, 1, 3, 0]
        assert validate_patient_id(None, self.entities._list_of_patients) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_validate_empty_text(self):
        self.entities._list_of_patients = [2, 1, 1, 3, 0]
        assert validate_patient_id(TEXT, self.entities._list_of_patients) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
