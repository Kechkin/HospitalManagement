import unittest

from Hospital import Hospital
from constants import ERROR_INPUT_INT, PATIENT_NOT_FOUND, ERROR_DECREASE, ERROR_EMPTY_VALUE, TEXT


class TestCheckDecreasePatient(unittest.TestCase):
    app = Hospital()

    def test_default_value(self):
        self.assertEqual(self.app.decrease_status_patient(2), 'Новый статус пациента: Тяжело болен')

    def test_check_text_instead_number(self):
        self.assertEqual(self.app.decrease_status_patient(TEXT), ERROR_INPUT_INT)

    def test_check_zero(self):
        self.assertEqual(self.app.decrease_status_patient(-12), PATIENT_NOT_FOUND)

    def test_check_max_id(self):
        self.assertEqual(self.app.decrease_status_patient(224), PATIENT_NOT_FOUND)

    def test_check_string_number(self):
        self.assertEqual(self.app.decrease_status_patient('12'), ERROR_INPUT_INT)

    def test_check_double_decrease(self):
        self.app.decrease_status_patient(25)
        self.assertEqual(self.app.decrease_status_patient(25), ERROR_DECREASE)

    def test_check_empty_value(self):
        self.assertEqual(self.app.decrease_status_patient(), ERROR_EMPTY_VALUE)

    def test_check_from_max_to_min(self):
        self.app._list_of_patients[54] = 3
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Слегка болен')
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Болен')
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Тяжело болен')
        self.assertEqual(self.app.decrease_status_patient(55), ERROR_DECREASE)
