from UseCases import UseCases
from HospitalEntities import HospitalEntities
from functions import generate_patients_with_statuses_from_zero_to_three


class TestProtectedMethods:
    entities = HospitalEntities()
    app = UseCases(entities)

    def test_get_new_patient_status(self):
        self.entities._list_of_patients = generate_patients_with_statuses_from_zero_to_three(10, 0)
        assert self.app._get_new_patient_status(8) == 'Новый статус пациента: Тяжело болен'

    def test_get_patient_by_id(self):
        self.entities._list_of_patients = generate_patients_with_statuses_from_zero_to_three(15, 0)
        # assert self.app._get_patient_by_id(12) == 0
        assert self.entities.get_patient_by_id(12) == 0
