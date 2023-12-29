from unittest.mock import patch
from UseCases import UseCases
from Hospital import Hospital
from constants import (PATIENT_DISCHARGED, PATIENT_STATUS_READY_TO_DISCHARGE, ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID,
                       YES, NO, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
from functions import generate_patients_with_statuses_from_zero_to_three


class TestIncreaseStatusPatient:
    entities = Hospital()
    app = UseCases(entities)

    @patch.object(UseCases, '_get_input')
    def test_ready_to_discharge_patient_from_database(self, mock_get_input):
        self.entities._list_of_patients = [3, 3, 1, 2]
        mock_get_input.return_value = YES
        assert self.app.increase_status_patient(1) == PATIENT_DISCHARGED
        assert self.entities._list_of_patients == [3, 1, 2]

    @patch.object(UseCases, '_get_input')
    def test_patient_not_ready_to_discharge(self, mock_get_input):
        self.entities._list_of_patients = [3, 3, 3, 2, 0]
        mock_get_input.return_value = NO
        assert self.app.increase_status_patient(1) == PATIENT_STATUS_READY_TO_DISCHARGE
        assert self.entities._list_of_patients == [3, 3, 3, 2, 0]

    def test_increase_statuses_patient(self):
        self.entities._list_of_patients = [0, 1, 3, 2, 0]
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Болен'
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Слегка болен'
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Готов к выписке'
        assert self.entities._list_of_patients == [3, 1, 3, 2, 0]

    def test_string_number(self):
        assert self.app.increase_status_patient('12') == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_empty_value(self):
        assert self.app.increase_status_patient('') == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_min_value(self):
        self.app._list_of_patients = generate_patients_with_statuses_from_zero_to_three(4, 2)
        assert self.app.increase_status_patient(-12) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_max_value(self):
        self.app._list_of_patients = generate_patients_with_statuses_from_zero_to_three(4, 2)
        assert self.app.increase_status_patient(22) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
