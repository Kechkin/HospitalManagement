from UseCases import UseCases
from Hospital import Hospital
from constants import ZERO
from functions import generate_patients_with_statuses_from_zero_to_three


class TestProtectedMethods:
    entities = Hospital()
    app = UseCases(entities)

    def test_get_patient_by_id(self):
        self.entities._list_of_patients = generate_patients_with_statuses_from_zero_to_three(15, 0)
        assert self.entities._get_status_number_by_patient_id(12) == ZERO
