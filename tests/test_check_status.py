import unittest

from Hospital import Status


class TestStatus(unittest.TestCase):
    st = Status()

    def test_different_statuses(self):
        self.assertEqual(self.st.get_status_patient(0), 'Тяжело болен')
        self.assertEqual(self.st.get_status_patient(1), 'Болен')
        self.assertEqual(self.st.get_status_patient(2), 'Слегка болен')
        self.assertEqual(self.st.get_status_patient(3), 'Готов к выписке')

    def test_check_empty_value(self):
        try:
            self.st.get_status_patient()
        except Exception as error:
            self.assertEqual(error.args[0],
                             "Status.get_status_patient() missing 1 required positional argument: 'status_id'")

    def test_check_different_value(self):
        self.assertEqual(self.st.get_status_patient(-12), None)
        self.assertEqual(self.st.get_status_patient(7), None)

    def test_check_text_value(self):
        self.assertEqual(self.st.get_status_patient('text'), None)
