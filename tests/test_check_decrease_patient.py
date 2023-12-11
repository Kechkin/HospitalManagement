import unittest

from Hospital import Hospital


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
        self.assertEqual(self.app.decrease_status_patient(), 'Ошибка. Пустое значение, введите число')

    def test_check_from_max_to_min(self):
        self.app._list_of_patients[54] = 3
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Слегка болен')
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Болен')
        self.assertEqual(self.app.decrease_status_patient(55), 'Новый статус пациента: Тяжело болен')
        self.assertEqual(self.app.decrease_status_patient(55), 'Ошибка. Нельзя понизить самый низкий '
                                                               'статус (наши пациенты не умирают)')
