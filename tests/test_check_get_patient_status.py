import unittest

from Hospital import Hospital
from constants import ERROR_INPUT_INT, ERROR_EMPTY_VALUE, PATIENT_NOT_FOUND, TEXT
from functions import generate_patients


class TestCheckGetPatientStatus(unittest.TestCase):
    app = Hospital()

    def test_check_patient_status(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.get_status_patient(100), 'Статус пациента: Слегка болен')

    def test_check_different_statuses(self):
        self.app._list_of_patients = generate_patients(200, 3)
        self.assertEqual(self.app.get_status_patient(100), 'Статус пациента: Готов к выписке')

        self.app.decrease_status_patient(100)
        self.assertEqual(self.app.get_status_patient(100), 'Статус пациента: Слегка болен')

        self.app.decrease_status_patient(100)
        self.assertEqual(self.app.get_status_patient(100), 'Статус пациента: Болен')

        self.app.decrease_status_patient(100)
        self.assertEqual(self.app.get_status_patient(100), 'Статус пациента: Тяжело болен')

    def test_check_input_text(self):
        self.app._list_of_patients = generate_patients(200, 3)
        self.assertEqual(self.app.get_status_patient(TEXT), ERROR_INPUT_INT)

    def test_check_input_empty_value(self):
        self.app._list_of_patients = generate_patients(200, 3)
        self.assertEqual(self.app.get_status_patient(), ERROR_EMPTY_VALUE)

    def test_check_error_values(self):
        self.app._list_of_patients = generate_patients(200, 3)
        self.assertEqual(self.app.get_status_patient(-10), PATIENT_NOT_FOUND)
        self.assertEqual(self.app.get_status_patient(301), PATIENT_NOT_FOUND)
