from UseCases import Status
from constants import TEXT


class TestStatus:
    st = Status()

    def test_different_statuses(self):
        assert self.st.get_status_patient(0) == 'Тяжело болен'
        assert self.st.get_status_patient(1) == 'Болен'
        assert self.st.get_status_patient(2) == 'Слегка болен'
        assert self.st.get_status_patient(3) == 'Готов к выписке'

    def test_empty_value(self):
        try:
            self.st.get_status_patient(None)
        except Exception as error:
            assert error.args[0] == "Status.get_status_patient() missing 1 required positional argument: 'status_id'"

    def test_different_out_of_value_max(self):
        assert self.st.get_status_patient(7) is None

    def test_different_out_of_value_min(self):
        assert self.st.get_status_patient(-12) is None

    def test_text_value(self):
        assert self.st.get_status_patient(TEXT) is None
