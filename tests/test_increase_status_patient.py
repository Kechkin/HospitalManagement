from unittest.mock import MagicMock

from DialogWithUser import DialogWithUser
from UseCases import UseCases
from Hospital import Hospital


class TestIncreaseStatusPatient:
    entities = Hospital()
    dialog = DialogWithUser()
    app = UseCases(entities, dialog)

    def test_with_the_highest_status_can_be_discharged_patient_if_user_approved(self):
        self.entities._list_of_patients = [3, 3, 1, 2]
        self.dialog.request_confirmation_for_patient_discharge = MagicMock(return_value=True)
        self.dialog.send_message = MagicMock()
        self.app.increase_patient_status(1)
        self.dialog.send_message.assert_called_with('Пациент выписан из больницы')
        assert self.entities._list_of_patients == [3, 1, 2]

    def test_if_user_refused_to_discharge_patient_then_status_remained_high(self):
        self.entities._list_of_patients = [3, 3, 2]
        self.dialog.request_confirmation_for_patient_discharge = MagicMock(return_value=False)
        self.dialog.send_message = MagicMock()
        self.app.increase_patient_status(1)
        self.dialog.send_message.assert_called_with('Пациент остался в статусе "Готов к выписке"')
        assert self.entities._list_of_patients == [3, 3, 2]

    def test_to_increase_from_lowest_to_highest_status(self):
        self.entities._list_of_patients = [0, 1, 3]
        self.dialog.send_message = MagicMock()
        self.app.increase_patient_status(1)
        self.dialog.send_message.assert_called_with('Новый статус пациента: "Болен"')
        self.app.increase_patient_status(1)
        self.dialog.send_message.assert_called_with('Новый статус пациента: "Слегка болен"')
        self.app.increase_patient_status(1)
        self.dialog.send_message.assert_called_with('Новый статус пациента: "Готов к выписке"')
        assert self.entities._list_of_patients == [3, 1, 3]

    def test_cannot_increase_status_when_patient_id_is_outside_list(self):
        self.entities._list_of_patients = [2, 2, 2, 2]
        self.dialog.send_message = MagicMock()
        self.app.increase_patient_status(22)
        self.dialog.send_message.assert_called_with('Ошибка. В больнице нет пациента с таким ID')


class TestCanIncreaseStatus:
    entities = Hospital()
    dialog = DialogWithUser()
    app = UseCases(entities, dialog)

    def test_if_not_allowed_increase_status_then_get_false(self):
        self.entities._list_of_patients = [3, 2, 1]
        assert self.entities.approve_to_increase_of_status(patient_id=1) is False

    def test_if_allowed_increase_status_then_get_true(self):
        self.entities._list_of_patients = [2, 2, 1]
        assert self.entities.approve_to_increase_of_status(patient_id=1) is True
