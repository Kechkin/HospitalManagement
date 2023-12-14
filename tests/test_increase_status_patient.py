from unittest.mock import patch
import HospitalApp
from HospitalApp import Hospital
from constants import (PATIENT_DISCHARGED, PATIENT_READY_TO_DISCHARGE, ERROR_INPUT_UNSIGNED_INT,
                       ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, YES, NO)
from functions import generate_patients_with_statuses


class TestCheckIncreaseStatusPatient:
    app = Hospital()

    @patch.object(HospitalApp.Patient, '_get_input')
    def test_ready_to_discharge_patient_from_database(self, mock_get_input):
        # Check that answer yes - discharged patient from database
        self.app._list_of_patients = [3]
        mock_get_input.return_value = YES
        assert self.app.increase_status_patient(1) == PATIENT_DISCHARGED
        # Check that List is empty
        assert self.app._list_of_patients == []

    @patch.object(HospitalApp.Patient, '_get_input')
    def test_patient_not_ready_to_discharge(self, mock_get_input):
        self.app._list_of_patients = [3]
        # Check that any answer except 'yes' -  patient stays in database
        mock_get_input.return_value = NO
        assert self.app.increase_status_patient(1) == PATIENT_READY_TO_DISCHARGE
        # Check that List isn't empty
        assert self.app._list_of_patients == [3]

    def test_increase_statuses_patient(self):
        self.app._list_of_patients = [0]
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Болен'
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Слегка болен'
        assert self.app.increase_status_patient(1) == 'Новый статус пациента: Готов к выписке'

    def test_string_number(self):
        assert self.app.increase_status_patient('12') == ERROR_INPUT_UNSIGNED_INT

    def test_empty_value(self):
        assert self.app.increase_status_patient('') == ERROR_INPUT_UNSIGNED_INT

    def test_max_and_min_values(self):
        self.app._list_of_patients = generate_patients_with_statuses(200, 2)
        assert self.app.increase_status_patient(-123) == ERROR_INPUT_UNSIGNED_INT
        assert self.app.increase_status_patient(224) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
