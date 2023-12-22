from unittest.mock import patch
import HospitalApp
from HospitalApp import Hospital
from Service import BaseLogic
from constants import (PATIENT_DISCHARGED, PATIENT_STATUS_READY_TO_DISCHARGE, ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID,
                       YES, NO, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
from functions import generate_patients_with_statuses


class TestIncreaseStatusPatient:
    service = BaseLogic()
    app = Hospital(service)

    @patch.object(HospitalApp.Patient, '_get_input')
    def test_ready_to_discharge_patient_from_database(self, mock_get_input):
        self.service._list_of_patients = [3, 3, 3, 2, 0]
        mock_get_input.return_value = YES
        assert self.app.increase_status_patient(1) == PATIENT_DISCHARGED
        assert self.service._list_of_patients == [3, 3, 2, 0]

    @patch.object(HospitalApp.Patient, '_get_input')
    def test_patient_not_ready_to_discharge(self, mock_get_input):
        self.service._list_of_patients = [3, 3, 3, 2, 0]
        mock_get_input.return_value = NO
        assert self.app.increase_status_patient(1) == PATIENT_STATUS_READY_TO_DISCHARGE
        assert self.service._list_of_patients == [3, 3, 3, 2, 0]

    def test_increase_statuses_patient(self):
        self.service._list_of_patients = [0, 1, 3, 2, 0]
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Болен'
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Слегка болен'
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Готов к выписке'
        assert self.service._list_of_patients == [3, 1, 3, 2, 0]

    def test_string_number(self):
        assert self.app.increase_status_patient('12') == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_empty_value(self):
        assert self.app.increase_status_patient('') == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_min_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(4, 2)
        assert self.app.increase_status_patient(-12) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_max_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(4, 2)
        assert self.app.increase_status_patient(22) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
