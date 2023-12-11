import unittest

from Hospital import Hospital
from constants import PATIENT_DISCHARGED, PATIENT_READY_TO_DISCHARGE, ERROR_INPUT_INT, ERROR_EMPTY_VALUE, PATIENT_NOT_FOUND
from functions import generate_patients


class TestCheckIncreaseStatusPatient(unittest.TestCase):
    app = Hospital()

    def test_check_all_increase_status_patient(self):
        self.app._list_of_patients = generate_patients(200, 0)
        self.assertEqual(self.app.increase_status_patient(100), 'Новый статус пациента: Болен')
        self.assertEqual(self.app.increase_status_patient(100), 'Новый статус пациента: Слегка болен')
        self.assertEqual(self.app.increase_status_patient(100), 'Новый статус пациента: Готов к выписке')

    def test_check_ready_to_discharge(self):
        self.assertEqual(self.app._input('да', 100), PATIENT_DISCHARGED)

    def test_check_not_ready_to_discharge(self):
        self.assertEqual(self.app._input('нет', 112), PATIENT_READY_TO_DISCHARGE)

    def test_check_string_number(self):
        self.assertEqual(self.app.increase_status_patient('12'), ERROR_INPUT_INT)

    def test_check_empty_value(self):
        self.assertEqual(self.app.increase_status_patient(), ERROR_EMPTY_VALUE)

    def test_check_max_and_min_values(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.increase_status_patient(-123), PATIENT_NOT_FOUND)
        self.assertEqual(self.app.increase_status_patient(224), PATIENT_NOT_FOUND)
