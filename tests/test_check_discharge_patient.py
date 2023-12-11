import unittest

from Hospital import Hospital
from functions import generate_patients


class TestCheckDischarge(unittest.TestCase):
    app = Hospital()

    def test_check_len_of_patients_list(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.app.discharge_patient(5)
        self.assertEqual(len(self.app._list_of_patients), 199)

    def test_repeat_discharge_patient(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.discharge_patient(200), 'Пациент выписан из больницы')
        self.assertEqual(self.app.discharge_patient(200), 'Ошибка. Такого пациента нет')

    def test_check_empty_list(self):
        self.app._list_of_patients = generate_patients(0, 2)
        self.assertEqual(self.app.discharge_patient(100), 'Ошибка. Такого пациента нет')

    def test_check_input_text(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.discharge_patient('100F'), 'Ошибка. Вводите число')

    def test_check_input_max_value(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.discharge_patient(10000), 'Ошибка. В больнице нет пациента с таким ID')

    def test_check_input_min_value(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.discharge_patient(-112), 'Ошибка. В больнице нет пациента с таким ID')

    def test_check_empty_value(self):
        self.app._list_of_patients = generate_patients(200, 2)
        self.assertEqual(self.app.discharge_patient(), 'Ошибка. Пустое значение, введите число')
