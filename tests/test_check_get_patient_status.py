from unittest.mock import patch

from UseCases import UseCases
from Hospital import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT


class TestGetPatientStatus:
    entities = Hospital()
    app = UseCases(entities)

    @patch('builtins.print')
    def test_patient_status(self, mock_print):
        self.entities._list_of_patients = [2, 2, 2, 2]
        self.app.get_status_patient(4)
        mock_print.assert_called_with('Статус пациента: Слегка болен')

    @patch('builtins.print')
    def test_different_statuses(self, mock_print):
        self.entities._list_of_patients = [3, 3, 3]
        self.app.get_status_patient(2)
        mock_print.assert_called_with('Статус пациента: Готов к выписке')

        self.entities._list_of_patients = [3, 2, 3]
        self.app.get_status_patient(2)
        mock_print.assert_called_with('Статус пациента: Слегка болен')

        self.entities._list_of_patients = [3, 1, 3]
        self.app.get_status_patient(2)
        mock_print.assert_called_with('Статус пациента: Болен')

        self.entities._list_of_patients = [3, 0, 3]
        self.app.get_status_patient(2)
        mock_print.assert_called_with('Статус пациента: Тяжело болен')

    @patch('builtins.print')
    def test_input_text(self, mock_print):
        self.entities._list_of_patients = [3, 3]
        self.app.get_status_patient(TEXT)
        mock_print.assert_called_with(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)

    @patch('builtins.print')
    def test_input_empty_value(self, mock_print):
        self.entities._list_of_patients = [3, 3]
        self.app.get_status_patient(None)
        mock_print.assert_called_with(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)

    @patch('builtins.print')
    def test_error_values(self, mock_print):
        self.entities._list_of_patients = [3, 3, 2]
        self.app.get_status_patient(-10)
        mock_print.assert_called_with(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
        self.app.get_status_patient(11)
        mock_print.assert_called_with(ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)
