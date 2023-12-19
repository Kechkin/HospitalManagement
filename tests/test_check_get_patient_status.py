from HospitalApp import Hospital
from constants import ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, TEXT, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
from functions import generate_patients_with_statuses


class TestGetPatientStatus:
    app = Hospital()

    def test_patient_status(self):
        self.app._list_of_patients = generate_patients_with_statuses(30, 2)
        assert self.app.get_status_patient(15) == 'Статус пациента: Слегка болен'

    def test_different_statuses(self):
        self.app._list_of_patients = generate_patients_with_statuses(4, 3)
        assert self.app.get_status_patient(2) == 'Статус пациента: Готов к выписке'

        self.app.decrease_status_patient(2)
        assert self.app.get_status_patient(2) == 'Статус пациента: Слегка болен'

        self.app.decrease_status_patient(2)
        assert self.app.get_status_patient(2) == 'Статус пациента: Болен'

        self.app.decrease_status_patient(2)
        assert self.app.get_status_patient(2) == 'Статус пациента: Тяжело болен'

    def test_input_text(self):
        self.app._list_of_patients = generate_patients_with_statuses(2, 3)
        assert self.app.get_status_patient(TEXT) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_input_empty_value(self):
        self.app._list_of_patients = generate_patients_with_statuses(2, 3)
        assert self.app.get_status_patient(None) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT

    def test_error_values(self):
        self.app._list_of_patients = generate_patients_with_statuses(10, 3)
        assert self.app.get_status_patient(-10) == ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
        assert self.app.get_status_patient(11) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
