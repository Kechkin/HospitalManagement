import unittest

from HospitalApp import Hospital
from constants import ERROR_INPUT_UNSIGNED_INT, ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT
from functions import generate_patients_with_statuses


class TestCheckGetPatientStatus(unittest.TestCase):
    app = Hospital()

    def test_check_patient_status(self):
        self.app._list_of_patients = generate_patients_with_statuses(200, 2)
        self.assertEqual(self.app.get_status_patient(100), 'Статус пациента: Слегка болен')

    def test_check_different_statuses(self):
        self.app._list_of_patients = generate_patients_with_statuses(4, 3)
        self.assertEqual(self.app.get_status_patient(2), 'Статус пациента: Готов к выписке')

        self.app.decrease_status_patient(2)
        self.assertEqual(self.app.get_status_patient(2), 'Статус пациента: Слегка болен')

        self.app.decrease_status_patient(2)
        self.assertEqual(self.app.get_status_patient(2), 'Статус пациента: Болен')

        self.app.decrease_status_patient(2)
        self.assertEqual(self.app.get_status_patient(2), 'Статус пациента: Тяжело болен')

    def test_check_input_text(self):
        self.app._list_of_patients = generate_patients_with_statuses(2, 3)
        self.assertEqual(self.app.get_status_patient(TEXT), ERROR_INPUT_UNSIGNED_INT)

    def test_check_input_empty_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(2, 3)
        self.assertEqual(self.app.get_status_patient(), ERROR_INPUT_UNSIGNED_INT)

    def test_check_error_values(self):
        self.app._list_of_patients = generate_patients_with_statuses(200, 3)
        self.assertEqual(self.app.get_status_patient(-10), ERROR_INPUT_UNSIGNED_INT)
        self.assertEqual(self.app.get_status_patient(301), ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)
