import unittest

from HospitalApp import Hospital
from constants import PATIENT_DISCHARGED, ERROR_THERE_IS_NO_PATIENT_ID, ERROR_INPUT_INT, ERROR_EMPTY_VALUE, \
    PATIENT_NOT_FOUND, TEXT
from functions import generate_patients


class TestCheckDischarge(unittest.TestCase):
    app = Hospital()

    def test_check_len_of_patients_list(self):
        self.app._list_of_patients = generate_patients(3, 2)
        self.app.discharge_patient(3)
        self.assertEqual(len(self.app._list_of_patients), 2)

    def test_repeat_discharge_patient(self):
        self.app._list_of_patients = generate_patients(1, 2)
        self.assertEqual(self.app.discharge_patient(1), PATIENT_DISCHARGED)
        self.assertEqual(self.app.discharge_patient(1), ERROR_THERE_IS_NO_PATIENT_ID)
        # Check that List is empty
        self.assertEqual(len(self.app._list_of_patients), 0)

    def test_check_empty_list(self):
        self.app._list_of_patients = generate_patients(0, 2)
        self.assertEqual(self.app.discharge_patient(100), ERROR_THERE_IS_NO_PATIENT_ID)

    def test_check_input_text(self):
        self.app._list_of_patients = generate_patients(3, 2)
        self.assertEqual(self.app.discharge_patient(TEXT), ERROR_INPUT_INT)

    def test_check_input_max_value(self):
        self.app._list_of_patients = generate_patients(3, 2)
        self.assertEqual(self.app.discharge_patient(10000), PATIENT_NOT_FOUND)

    def test_check_input_min_value(self):
        self.app._list_of_patients = generate_patients(3, 2)
        self.assertEqual(self.app.discharge_patient(-112), PATIENT_NOT_FOUND)

    def test_check_empty_value(self):
        self.app._list_of_patients = generate_patients(3, 2)
        self.assertEqual(self.app.discharge_patient(), ERROR_EMPTY_VALUE)
