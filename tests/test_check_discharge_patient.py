from UseCases import UseCases
from Hospital import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from functions import generate_patients_with_statuses_from_zero_to_three


class TestDischarge:
    entities = Hospital()
    app = UseCases(entities)

    def test_len_of_patients_list(self):
        self.entities._list_of_patients = [1, 2, 1]
        self.app.discharge_patient_from_list(3)
        assert self.entities._list_of_patients == [1, 2]

    def test_empty_list(self):
        assert self.app.discharge_patient_from_list(100) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def test_input_text(self):
        self.app._list_of_patients = generate_patients_with_statuses_from_zero_to_three(3, 2)
        assert self.app.discharge_patient_from_list(TEXT) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_input_max_value(self):
        self.app._list_of_patients = generate_patients_with_statuses_from_zero_to_three(3, 2)
        assert self.app.discharge_patient_from_list(300) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def test_input_min_value(self):
        self.app._list_of_patients = generate_patients_with_statuses_from_zero_to_three(3, 2)
        assert self.app.discharge_patient_from_list(-11) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_empty_value(self):
        self.app._list_of_patients = generate_patients_with_statuses_from_zero_to_three(3, 2)
        assert self.app.discharge_patient_from_list(None) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
