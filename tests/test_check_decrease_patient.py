import unittest

from HospitalApp import Hospital
from constants import ERROR_INPUT_INT, PATIENT_NOT_FOUND, ERROR_DECREASE, ERROR_EMPTY_VALUE, TEXT
from functions import generate_patients


class TestCheckDecreasePatient(unittest.TestCase):
    app = Hospital()

    def test_default_value(self):
        self.app._list_of_patients = generate_patients(3, 1)
        self.assertEqual(self.app.decrease_status_patient(2), 'Новый статус пациента: Тяжело болен')
        # Check that patient has status 0
        self.assertEqual(self.app._list_of_patients[1], 0)
        # Check that List isn't empty
        self.assertEqual(len(self.app._list_of_patients), 3)

    def test_check_text_instead_number(self):
        self.assertEqual(self.app.decrease_status_patient(TEXT), ERROR_INPUT_INT)

    def test_check_zero(self):
        self.assertEqual(self.app.decrease_status_patient(-12), PATIENT_NOT_FOUND)

    def test_check_max_id(self):
        self.assertEqual(self.app.decrease_status_patient(224), PATIENT_NOT_FOUND)

    def test_check_string_number(self):
        self.assertEqual(self.app.decrease_status_patient('12'), ERROR_INPUT_INT)

    def test_check_double_decrease(self):
        self.app._list_of_patients = generate_patients(3, 1)
        self.app.decrease_status_patient(3)
        self.assertEqual(self.app.decrease_status_patient(3), ERROR_DECREASE)
        # Check that List didn't change
        self.assertEqual(len(self.app._list_of_patients), 3)

    def test_check_empty_value(self):
        self.assertEqual(self.app.decrease_status_patient(), ERROR_EMPTY_VALUE)

    def test_check_from_max_to_min(self):
        self.app._list_of_patients = generate_patients(5, 1)
        self.app._list_of_patients[4] = 3
        # Check that status changed and equal 2
        self.assertEqual(self.app.decrease_status_patient(5), 'Новый статус пациента: Слегка болен')
        self.assertEqual(self.app._list_of_patients[4], 2)
        # Check that status changed and equal 1
        self.assertEqual(self.app.decrease_status_patient(5), 'Новый статус пациента: Болен')
        self.assertEqual(self.app._list_of_patients[4], 1)
        # Check that status changed and equal 0
        self.assertEqual(self.app.decrease_status_patient(5), 'Новый статус пациента: Тяжело болен')
        self.assertEqual(self.app._list_of_patients[4], 0)

    def test_check_max_decrease(self):
        self.assertEqual(self.app.decrease_status_patient(5), ERROR_DECREASE)

