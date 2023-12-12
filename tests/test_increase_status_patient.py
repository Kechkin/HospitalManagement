import unittest
from unittest.mock import patch

import HospitalApp
from HospitalApp import Hospital
from constants import PATIENT_DISCHARGED, PATIENT_READY_TO_DISCHARGE, ERROR_INPUT_INT, ERROR_EMPTY_VALUE, \
    PATIENT_NOT_FOUND, YES, NO, ZERO, ONE
from functions import generate_patients


class TestCheckIncreaseStatusPatient(unittest.TestCase):
    app = Hospital()

    @patch.object(HospitalApp.Patient, '_get_input')
    def test_check_ready_to_discharge(self, mock_get_input):
        # Check that answer yes - discharged patient from database
        self.app._list_of_patients = generate_patients(1, 3)
        mock_get_input.return_value = YES
        self.assertEqual(self.app.increase_status_patient(1), PATIENT_DISCHARGED)
        # Check that List is empty
        self.assertEqual(len(self.app._list_of_patients), ZERO)

    @patch.object(HospitalApp.Patient, '_get_input')
    def test_check_not_ready_to_discharge(self, mock_get_input):
        self.app._list_of_patients = generate_patients(1, 3)
        # Check that any answer except 'yes' -  patient stays in database
        mock_get_input.return_value = NO
        self.assertEqual(self.app.increase_status_patient(1), PATIENT_READY_TO_DISCHARGE)
        # Check that List isn't empty
        self.assertEqual(len(self.app._list_of_patients), ONE)

    def test_check_all_increase_status_patient(self):
        self.app._list_of_patients = generate_patients(1, 0)
        self.assertEqual(self.app.increase_status_patient(1), 'Новый статус пациента: Болен')
        self.assertEqual(self.app.increase_status_patient(1), 'Новый статус пациента: Слегка болен')
        self.assertEqual(self.app.increase_status_patient(1), 'Новый статус пациента: Готов к выписке')

    def test_check_string_number(self):
        self.assertEqual(self.app.increase_status_patient('12'), ERROR_INPUT_INT)

    def test_check_empty_value(self):
        self.assertEqual(self.app.increase_status_patient(), ERROR_EMPTY_VALUE)

    def test_check_max_and_min_values(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.increase_status_patient(-123), PATIENT_NOT_FOUND)
        self.assertEqual(self.app.increase_status_patient(224), PATIENT_NOT_FOUND)
