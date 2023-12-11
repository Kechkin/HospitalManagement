import unittest

from Hospital import Hospital
from constants import PATIENT_DISCHARGED, PATIENT_NOT_FOUND, PATIENT_READY_TO_DISCHARGE, YES, NO, TEXT
from functions import generate_patients


class TestCheckProtectedMethods(unittest.TestCase):
    app = Hospital()

    def test_check_input_yes(self):
        self.app._list_of_patients = generate_patients(200, 0)

        self.assertEqual(self.app._get_result_from_input_answer(150, YES), PATIENT_DISCHARGED)

        self.assertEqual(self.app._get_result_from_input_answer(-150, YES), PATIENT_NOT_FOUND)

        self.assertEqual(self.app._get_result_from_input_answer(350, YES), PATIENT_NOT_FOUND)

    def test_check_input_no(self):
        self.app._list_of_patients = generate_patients(200, 0)
        self.assertEqual(self.app._get_result_from_input_answer(50, NO),
                         PATIENT_READY_TO_DISCHARGE)

        self.assertEqual(self.app._get_result_from_input_answer(20, TEXT),
                         PATIENT_READY_TO_DISCHARGE)

        self.assertEqual(self.app._get_result_from_input_answer(50), PATIENT_READY_TO_DISCHARGE)

    def test_check_get_new_patient_status(self):
        self.app._list_of_patients = generate_patients(200, 0)
        self.assertEqual(self.app._get_new_patient_status(12), 'Новый статус пациента: Тяжело болен')

    def test_check_get_patient_by_id(self):
        self.app._list_of_patients = generate_patients(200, 0)
        self.assertEqual(self.app._get_patient_by_id(12), 0)
