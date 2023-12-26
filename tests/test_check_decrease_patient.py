from UseCases import UseCases
from HospitalEntities import HospitalEntities
from constants import (ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, ERROR_CANNOT_DECREASE_LOW_STATUS, TEXT,
                       ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)


class TestDecreasePatient:
    entities = HospitalEntities()
    app = UseCases(entities)

    def test_decrease_patient(self):
        self.entities._list_of_patients = [2, 1, 2, 0, 1]
        assert self.app.decrease_status_patient(2) == 'Новый статус пациента: Тяжело болен'
        assert self.entities._list_of_patients == [2, 0, 2, 0, 1]

    def test_text_instead_number(self):
        assert self.app.decrease_status_patient(TEXT) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_value_below_zero(self):
        assert self.app.decrease_status_patient(-12) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_max_id(self):
        assert self.app.decrease_status_patient(224) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID

    def test_double_decrease(self):
        self.entities._list_of_patients = [2, 1, 2, 0, 1]
        self.app.decrease_status_patient(2)
        assert self.app.decrease_status_patient(2) == ERROR_CANNOT_DECREASE_LOW_STATUS
        assert self.entities._list_of_patients == [2, 0, 2, 0, 1]

    def test_empty_value(self):
        assert self.app.decrease_status_patient(None) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_decrease_from_max_to_min_status(self):
        self.entities._list_of_patients = [3, 2, 3, 2, 3]
        assert self.app.decrease_status_patient(5) == 'Новый статус пациента: Слегка болен'
        assert self.entities._list_of_patients == [3, 2, 3, 2, 2]

        assert self.app.decrease_status_patient(5) == 'Новый статус пациента: Болен'
        assert self.entities._list_of_patients == [3, 2, 3, 2, 1]

        assert self.app.decrease_status_patient(5) == 'Новый статус пациента: Тяжело болен'
        assert self.entities._list_of_patients == [3, 2, 3, 2, 0]

    def test_max_decrease(self):
        self.entities._list_of_patients = [3, 2, 3, 2, 0]
        assert self.app.decrease_status_patient(5) == ERROR_CANNOT_DECREASE_LOW_STATUS
