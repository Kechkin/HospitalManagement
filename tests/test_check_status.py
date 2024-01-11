from Hospital import Hospital


class TestStatus:
    hospital = Hospital()

    def test_different_statuses(self):
        # тест, чтобы получить имя статуса по айди пациента
        # test_to_get_status_name_on_patients_id
        self.hospital._list_of_patients = [0, 1, 2, 3]
        assert self.hospital.get_status_name_by_patient_id(patient_id=1) == 'Тяжело болен'
        assert self.hospital.get_status_name_by_patient_id(patient_id=2) == 'Болен'
        assert self.hospital.get_status_name_by_patient_id(patient_id=3) == 'Слегка болен'
        assert self.hospital.get_status_name_by_patient_id(patient_id=4) == 'Готов к выписке'
