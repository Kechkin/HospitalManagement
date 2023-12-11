import unittest

from Hospital import Hospital
from functions import generate_patients


class TestCalculateStatistics(unittest.TestCase):
    app = Hospital()

    def test_default_calculate(self):
        self.app._list_of_patients = generate_patients(200, 1)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 200 чел., '
                                                          'из них: в статусе "Болен": 200 чел.')

    def test_check_patient_status_zero(self):
        self.app._list_of_patients = generate_patients(200, 0)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 200 чел., '
                                                          'из них: в статусе "Тяжело болен": 200 чел.')

    def test_check_patient_status_three(self):
        self.app._list_of_patients = generate_patients(200, 3)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 200 чел., из них: '
                                                          'в статусе "Готов к выписке": 200 чел.')

    def test_check_patient_status_two(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 200 чел., '
                                                          'из них: в статусе "Слегка болен": 200 чел.')

    def test_check_all_discharge_patient(self):
        self.app._list_of_patients = generate_patients(0, 2)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 0 чел., из них: ')

    def test_check_different_variants(self):
        self.app._list_of_patients = generate_patients(200, 1)
        self.app.decrease_status_patient(2)
        self.app.increase_status_patient(5)
        self.app.increase_status_patient(10)
        self.app.increase_status_patient(10)
        self.assertEqual(self.app.calculate_statistics(), 'В больнице на данный момент находится 200 чел., из них: '
                                                          'в статусе "Тяжело болен": 1 чел.в статусе "Болен": 197 чел.в статусе '
                                                          '"Слегка болен": 1 чел.в статусе "Готов к выписке": 1 чел.')

    def test_check_stop(self):
        self.assertEqual(self.app.stop(), 'Сеанс завершён.')
