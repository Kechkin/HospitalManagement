from unittest.mock import patch

from UseCases import UseCases
from Hospital import Hospital
from constants import (ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, ERROR_CANNOT_DECREASE_LOW_STATUS, TEXT,
                       ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)


class TestDecreasePatient:
    entities = Hospital()
    app = UseCases(entities)

    @patch('builtins.print')
    def test_decrease_patient(self, mock_print):
        self.entities._list_of_patients = [2, 1, 2]
        self.app.decrease_status_patient(2)
        mock_print.assert_called_with('Новый статус пациента: Тяжело болен')
        assert self.entities._list_of_patients == [2, 0, 2]

    @patch('builtins.print')
    def test_max_id(self, mock_print):
        self.app.decrease_status_patient(224)
        mock_print.assert_called_with(ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

    @patch('builtins.print')
    def test_double_decrease(self, mock_print):
        self.entities._list_of_patients = [2, 1, 2]
        self.app.decrease_status_patient(2)
        self.app.decrease_status_patient(2)
        mock_print.assert_called_with(ERROR_CANNOT_DECREASE_LOW_STATUS)
        assert self.entities._list_of_patients == [2, 0, 2]

    @patch('builtins.print')
    def test_decrease_from_max_to_min_status(self, mock_print):
        self.entities._list_of_patients = [3, 2, 3, 2, 3]
        self.app.decrease_status_patient(5)
        mock_print.assert_called_with('Новый статус пациента: Слегка болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 2]

        self.app.decrease_status_patient(5)
        mock_print.assert_called_with('Новый статус пациента: Болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 1]

        self.app.decrease_status_patient(5)
        mock_print.assert_called_with('Новый статус пациента: Тяжело болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 0]

    @patch('builtins.print')
    def test_max_decrease(self, mock_print):
        self.entities._list_of_patients = [3, 2, 0]
        self.app.decrease_status_patient(3)
        mock_print.assert_called_with(ERROR_CANNOT_DECREASE_LOW_STATUS)


class TestCanDecreaseStatus:
    entities = Hospital()
    app = UseCases(entities)

    def test_can_not_decrease_status_patient_id_get_false(self):
        self.entities._list_of_patients = [0, 2, 1]
        assert self.entities.can_decrease_status_patient_id(patient_id=1) is False

    def test_can_increase_status_get_none(self):
        self.entities._list_of_patients = [3, 1, 2]
        assert self.entities.can_decrease_status_patient_id(patient_id=1) is None
