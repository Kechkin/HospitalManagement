from unittest.mock import MagicMock

from DialogueWithTheUser import DialogueWithTheUser
from UseCases import UseCases
from Hospital import Hospital


class TestIncreaseStatusPatient:
    entities = Hospital()
    dialog = DialogueWithTheUser()
    app = UseCases(entities, dialog)

    def test_ready_to_discharge_patient(self):
        self.entities._list_of_patients = [3, 3, 1, 2]
        self.dialog.request_confirmation_to_discharge_patient = MagicMock(return_value=True)
        self.dialog.send_message = MagicMock()
        self.app.increase_status_patient(1)
        self.dialog.send_message.assert_called_with('Пациент выписан из больницы')
        assert self.entities._list_of_patients == [3, 1, 2]

    def test_patient_not_ready_to_discharge(self):
        self.entities._list_of_patients = [3, 3, 2]
        self.dialog.request_confirmation_to_discharge_patient = MagicMock(return_value=False)
        self.dialog.send_message = MagicMock()
        self.app.increase_status_patient(1)
        self.dialog.send_message.assert_called_with('Пациент остался в статусе "Готов к выписке"')
        assert self.entities._list_of_patients == [3, 3, 2]

    def test_increase_statuses_patient(self):
        self.entities._list_of_patients = [0, 1, 3]
        self.dialog.send_message = MagicMock()
        self.app.increase_status_patient(1)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Болен')
        self.app.increase_status_patient(1)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Слегка болен')
        self.app.increase_status_patient(1)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Готов к выписке')
        assert self.entities._list_of_patients == [3, 1, 3]

    def test_max_value(self):
        self.entities._list_of_patients = [2, 2, 2, 2]
        self.dialog.send_message = MagicMock()
        self.app.increase_status_patient(22)
        self.dialog.send_message.assert_called_with('Ошибка. В больнице нет пациента с таким ID')


class TestCanIncreaseStatus:
    entities = Hospital()
    dialog = DialogueWithTheUser()
    app = UseCases(entities, dialog)

    def test_can_not_increase_status_patient_id_get_false(self):
        self.entities._list_of_patients = [3, 2, 1]
        assert self.entities.can_increase_status_patient(patient_id=1) is False

    def test_can_increase_status_get_none(self):
        self.entities._list_of_patients = [2, 2, 1]
        assert self.entities.can_increase_status_patient(patient_id=1) is True
