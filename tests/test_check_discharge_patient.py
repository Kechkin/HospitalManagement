import unittest

from HospitalApp import Hospital
from constants import PATIENT_DISCHARGED, ERROR_THERE_IS_NO_PATIENT_ID, ERROR_INPUT_UNSIGNED_INT, ERROR_EMPTY_VALUE_INPUT_UNSIGNED_INT, \
    ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT
from functions import generate_patients_with_statuses


class TestCheckDischarge(unittest.TestCase):
    app = Hospital()

    def test_check_len_of_patients_list(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        self.app.discharge_patient(3)
        self.assertEqual(len(self.app._list_of_patients), 2)

    def test_repeat_discharge_patient(self):
        self.app._list_of_patients = generate_patients_with_statuses(1, 2)
        self.assertEqual(self.app.discharge_patient(1), PATIENT_DISCHARGED)
        self.assertEqual(self.app.discharge_patient(1), ERROR_THERE_IS_NO_PATIENT_ID)
        # Check that List is empty
        self.assertEqual(len(self.app._list_of_patients), 0)

    def test_check_empty_list(self):
        self.app._list_of_patients = generate_patients_with_statuses(0, 2)
        self.assertEqual(self.app.discharge_patient(100), ERROR_THERE_IS_NO_PATIENT_ID)

    def test_check_input_text(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        self.assertEqual(self.app.discharge_patient(TEXT), ERROR_INPUT_UNSIGNED_INT)

    def test_check_input_max_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        self.assertEqual(self.app.discharge_patient(10000), ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)

    def test_check_input_min_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        self.assertEqual(self.app.discharge_patient(-112), ERROR_INPUT_UNSIGNED_INT)

    def test_check_empty_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(3, 2)
        self.assertEqual(self.app.discharge_patient(), ERROR_INPUT_UNSIGNED_INT)
