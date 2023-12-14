import unittest

from HospitalApp import Hospital
from functions import generate_patients_with_statuses


class TestCheckProtectedMethods(unittest.TestCase):
    app = Hospital()

    def test_check_get_new_patient_status(self):
        self.app._list_of_patients = generate_patients_with_statuses(200, 0)
        self.assertEqual(self.app._get_new_patient_status(12), 'Новый статус пациента: Тяжело болен')

    def test_check_get_patient_by_id(self):
        self.app._list_of_patients = generate_patients_with_statuses(200, 0)
        self.assertEqual(self.app._get_patient_by_id(12), 0)
