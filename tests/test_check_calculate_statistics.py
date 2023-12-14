import unittest

from HospitalApp import Hospital
from functions import generate_patients_with_statuses


class TestCalculateStatistics(unittest.TestCase):
    app = Hospital()

    def test_default_calculate(self):
        self.app._list_of_patients = generate_patients_with_statuses(5, 1)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 5 чел., '
                                                          'из них: в статусе "Болен": 5 чел.')

    def test_check_patient_status_zero(self):
        self.app._list_of_patients = generate_patients_with_statuses(5, 0)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 5 чел., '
                                                          'из них: в статусе "Тяжело болен": 5 чел.')

    def test_check_patient_status_three(self):
        self.app._list_of_patients = generate_patients_with_statuses(5, 3)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 5 чел., из них: '
                                                          'в статусе "Готов к выписке": 5 чел.')

    def test_check_patient_status_two(self):
        self.app._list_of_patients = generate_patients_with_statuses(5, 2)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 5 чел., '
                                                          'из них: в статусе "Слегка болен": 5 чел.')

    def test_check_all_discharge_patient(self):
        self.app._list_of_patients = generate_patients_with_statuses(0, 2)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 0 чел., '
                                                          'из них: ')

    def test_check_different_variants(self):
        self.app._list_of_patients = generate_patients_with_statuses(10, 1)
        self.app._list_of_patients[1] = 3
        self.app._list_of_patients[4] = 1
        self.app._list_of_patients[7] = 2
        self.app._list_of_patients[6] = 0
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 10 чел., '
                                                          'из них: в статусе "Тяжело болен": 1 чел.в статусе "Болен": '
                                                          '7 чел.в статусе "Слегка болен": 1 чел.в статусе '
                                                          '"Готов к выписке": 1 чел.')

    def test_check_stop(self):
        self.assertEqual(self.app.stop(), 'Сеанс завершён.')
