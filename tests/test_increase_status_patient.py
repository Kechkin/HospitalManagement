from unittest.mock import patch, MagicMock

from DialogueWithTheUser import DialogueWithTheUser
from UseCases import UseCases
from Hospital import Hospital
from constants import (PATIENT_DISCHARGED, PATIENT_STATUS_READY_TO_DISCHARGE, ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID,
                       YES, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT, TEXT, NO)


class TestIncreaseStatusPatient:
    entities = Hospital()
    app = UseCases(entities)

    @patch('builtins.print')
    def test_ready_to_discharge_patient(self, mock_print):
        self.entities._list_of_patients = [3, 3, 1, 2]
        self.app._ask_client_to_discharge_patient = MagicMock(return_value=True)
        self.app.increase_status_patient(1)

        mock_print.assert_called_with(PATIENT_DISCHARGED)
        assert self.entities._list_of_patients == [3, 1, 2]

    @patch('builtins.print')
    def test_patient_not_ready_to_discharge(self, mock_print):
        self.entities._list_of_patients = [3, 3, 2]
        self.app._ask_client_to_discharge_patient = MagicMock(return_value=False)
        self.app.increase_status_patient(1)

        mock_print.assert_called_with(PATIENT_STATUS_READY_TO_DISCHARGE)
        assert self.entities._list_of_patients == [3, 3, 2]

    @patch('builtins.print')
    def test_increase_statuses_patient(self, mock_print):
        self.entities._list_of_patients = [0, 1, 3]
        self.app.increase_status_patient(1)
        mock_print.assert_called_with('Новый статус пациента: Болен')
        self.app.increase_status_patient(1)
        mock_print.assert_called_with('Новый статус пациента: Слегка болен')
        self.app.increase_status_patient(1)
        mock_print.assert_called_with('Новый статус пациента: Готов к выписке')
        assert self.entities._list_of_patients == [3, 1, 3]

    @patch('builtins.print')
    def test_max_value(self, mock_print):
        self.entities._list_of_patients = [2, 2, 2, 2]
        self.app.increase_status_patient(22)
        mock_print.assert_called_with(ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)


class TestCanIncreaseStatus:
    entities = Hospital()
    app = UseCases(entities)

    def test_can_not_increase_status_patient_id_get_false(self):
        self.entities._list_of_patients = [3, 2, 1]
        assert self.entities.can_increase_status_patient_id(patient_id=1) is False

    def test_can_increase_status_get_none(self):
        self.entities._list_of_patients = [2, 2, 1]
        assert self.entities.can_increase_status_patient_id(patient_id=1) is None


class TestProtectedMethods:
    entities = Hospital()
    app = UseCases(entities)

    def test_ask_client_to_discharge_patient_get_true(self):
        DialogueWithTheUser.get_message_to_discharge_patient = MagicMock(return_value=YES)
        assert self.app._ask_client_to_discharge_patient() is True

    def test_get_status_from_client_answer_no(self):
        DialogueWithTheUser.get_message_to_discharge_patient = MagicMock(return_value=NO)
        assert self.app._ask_client_to_discharge_patient() is False

    def test_get_status_from_client_answer_some_text(self):
        DialogueWithTheUser.get_message_to_discharge_patient = MagicMock(return_value=TEXT)
        assert self.app._ask_client_to_discharge_patient() is False
