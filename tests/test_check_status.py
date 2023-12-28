from Hospital import Hospital


class TestStatus:
    st = Hospital()

    def test_different_statuses(self):
        self.st._list_of_patients = [0, 1, 2, 3]
        assert self.st.get_status_name_by_patient_id(patient_id=1) == 'Тяжело болен'
        assert self.st.get_status_name_by_patient_id(patient_id=2) == 'Болен'
        assert self.st.get_status_name_by_patient_id(patient_id=3) == 'Слегка болен'
        assert self.st.get_status_name_by_patient_id(patient_id=4) == 'Готов к выписке'

    def test_different_out_of_value_max(self):
        self.st._list_of_patients = [0, 1, 10]
        assert self.st.get_status_name_by_patient_id(patient_id=3) is None

    def test_different_out_of_value_min(self):
        self.st._list_of_patients = [0, 1, -10]
        assert self.st.get_status_name_by_patient_id(3) is None

