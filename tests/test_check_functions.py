import unittest

from constants import ERROR_INPUT_INT, ERROR_EMPTY_VALUE, PATIENT_NOT_FOUND
from functions import check_patient_id


class TestFunction:
    @check_patient_id
    def victim_test(self, patient_id):
        return f'функция вернула значение: {patient_id}'


class TestCheckDischarge(unittest.TestCase):
    test_func = TestFunction()

    def test_check_validate_func(self):
        patient_id = 15
        self.assertEqual(self.test_func.victim_test(15), f'функция вернула значение: {patient_id}')

    def test_check_validate_text(self):
        self.assertEqual(self.test_func.victim_test('text'), ERROR_INPUT_INT)

    def test_check_validate_empty_value(self):
        self.assertEqual(self.test_func.victim_test(), ERROR_EMPTY_VALUE)

    def test_check_validate_max_mix_value(self):
        self.assertEqual(self.test_func.victim_test(214), PATIENT_NOT_FOUND)
        self.assertEqual(self.test_func.victim_test(-14), PATIENT_NOT_FOUND)
