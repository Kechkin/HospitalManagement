from unittest.mock import patch

from UseCases import UseCases
from Hospital import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT, \
    PATIENT_DISCHARGED
from functions import generate_patients_with_statuses_from_zero_to_three


class TestDischarge:
    entities = Hospital()
    app = UseCases(entities)

    @patch('builtins.print')
    def test_len_of_patients_list(self, mock_print):
        self.entities._list_of_patients = [1, 2, 1]
        self.app.discharge_patient(3)
        mock_print.assert_called_with(PATIENT_DISCHARGED)
        assert self.entities._list_of_patients == [1, 2]

    @patch('builtins.print')
    def test_empty_list(self, mock_print):
        self.entities._list_of_patients = [1, 2, 1]
        self.app.discharge_patient(100)
        mock_print.assert_called_with(ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

    @patch('builtins.print')
    def test_input_max_value(self, mock_print):
        self.entities._list_of_patients = generate_patients_with_statuses_from_zero_to_three(3, 2)
        self.app.discharge_patient(300)
        mock_print.assert_called_with(ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

