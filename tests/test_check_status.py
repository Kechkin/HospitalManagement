from Hospital import Hospital


class TestStatus:
    hospital = Hospital()

    def test_different_statuses(self):
        self.hospital._list_of_patients = [0, 1, 2, 3]
        assert self.hospital.get_status_name_by_patient_id(patient_id=1) == 'Тяжело болен'
        assert self.hospital.get_status_name_by_patient_id(patient_id=2) == 'Болен'
        assert self.hospital.get_status_name_by_patient_id(patient_id=3) == 'Слегка болен'
        assert self.hospital.get_status_name_by_patient_id(patient_id=4) == 'Готов к выписке'

    def test_different_out_of_value_max(self):
        self.hospital._list_of_patients = [0, 1, 10]
        assert self.hospital.get_status_name_by_patient_id(patient_id=3) is None

    def test_different_out_of_value_min(self):
        self.hospital._list_of_patients = [0, 1, -10]
        assert self.hospital.get_status_name_by_patient_id(3) is None

