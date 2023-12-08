import unittest

from Hospital import Hospital
from functions import generate_patients


class TestCalculateStatistics(unittest.TestCase):
    app = Hospital()

    def test_default_calculate(self):
        self.app._list_of_patients = generate_patients(200, 1)
        compare = 'В больнице на данный момент находится 200 чел., из них: в статусе "Болен": 200 чел.'
        self.assertEqual(self.app.calculate_statistics(), compare)

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


class TestCheckDecreasePatient(unittest.TestCase):
    app = Hospital()

    def test_default_value(self):
        self.assertEqual(self.app.decrease_status_patient(2), 'Новый статус пациента: Тяжело болен')

    def test_check_text_instead_number(self):
        self.assertEqual(self.app.decrease_status_patient('text'), 'Ошибка. Вводите число')

    def test_check_zero(self):
        self.assertEqual(self.app.decrease_status_patient(-12), 'Ошибка. В больнице нет пациента с таким ID')

    def test_check_max_id(self):
        self.assertEqual(self.app.decrease_status_patient(224), 'Ошибка. В больнице нет пациента с таким ID')

    def test_check_string_number(self):
        self.assertEqual(self.app.decrease_status_patient('12'), 'Ошибка. Вводите число')

    def test_check_double_decrease(self):
        self.app.decrease_status_patient(25)
        self.assertEqual(self.app.decrease_status_patient(25), 'Ошибка. Нельзя понизить самый низкий статус '
                                                               '(наши пациенты не умирают)')

    def test_check_empty_value(self):
        # Todo validate empty values
        self.assertEqual(self.app.decrease_status_patient(), 'Ошибка. Вводите число')

    def test_check_from_max_to_min(self):
        self.app._list_of_patients[54] = 3
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Слегка болен')
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Болен')
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Тяжело болен')
        self.assertEqual(self.app.decrease_status_patient(55), 'Ошибка. Нельзя понизить самый низкий '
                                                               'статус (наши пациенты не умирают)')
