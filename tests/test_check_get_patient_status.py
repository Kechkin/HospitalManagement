from UseCases import UseCases
from Hospital import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from functions import generate_patients_with_statuses_from_zero_to_three


class TestGetPatientStatus:
    entities = Hospital()
    app = UseCases(entities)

    def test_patient_status(self):
        self.entities._list_of_patients = [2, 2, 2, 2]
        assert self.app.get_status_patient(4) == 'Статус пациента: Слегка болен'

    def test_different_statuses(self):
        self.entities._list_of_patients = [3, 3, 3]
        assert self.app.get_status_patient(2) == 'Статус пациента: Готов к выписке'

        self.app.get_decrease_new_status_patient(2)
        assert self.app.get_status_patient(2) == 'Статус пациента: Слегка болен'

        self.app.get_decrease_new_status_patient(2)
        assert self.app.get_status_patient(2) == 'Статус пациента: Болен'

        self.app.get_decrease_new_status_patient(2)
        assert self.app.get_status_patient(2) == 'Статус пациента: Тяжело болен'

    def test_input_text(self):
        self.entities._list_of_patients = [3, 3]
        assert self.app.get_status_patient(TEXT) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_input_empty_value(self):
        self.entities._list_of_patients = [3, 3]
        assert self.app.get_status_patient(None) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_error_values(self):
        self.entities._list_of_patients = [3, 3, 2]
        assert self.app.get_status_patient(-10) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
        assert self.app.get_status_patient(11) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
