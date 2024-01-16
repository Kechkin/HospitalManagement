from unittest.mock import MagicMock

from DialogWithUser import DialogWithUser
from UseCases import UseCases
from Hospital import Hospital


class TestGetPatientStatus:
    entities = Hospital()
    dialog = DialogWithUser()
    app = UseCases(entities, dialog)

    def test_patient_status(self):
        self.entities._list_of_patients = [2, 2, 2, 2]
        self.dialog.send_message = MagicMock()
        self.app.get_patient_status(4)
        self.dialog.send_message.assert_called_with('Статус пациента: "Слегка болен"')

    def test_to_get_different_patient_statuses(self):
        self.entities._list_of_patients = [3, 3, 3]
        self.dialog.send_message = MagicMock()
        self.app.get_patient_status(2)
        self.dialog.send_message.assert_called_with('Статус пациента: "Готов к выписке"')

        self.entities._list_of_patients = [3, 2, 3]
        self.app.get_patient_status(2)
        self.dialog.send_message.assert_called_with('Статус пациента: "Слегка болен"')

        self.entities._list_of_patients = [3, 1, 3]
        self.app.get_patient_status(2)
        self.dialog.send_message.assert_called_with('Статус пациента: "Болен"')

        self.entities._list_of_patients = [3, 0, 3]
        self.app.get_patient_status(2)
        self.dialog.send_message.assert_called_with('Статус пациента: "Тяжело болен"')

    def test_cannot_get_status_when_patient_id_is_outside_list(self):
        self.entities._list_of_patients = [3, 3, 2]
        self.dialog.send_message = MagicMock()
        self.app.get_patient_status(11)
        self.dialog.send_message.assert_called_with('Ошибка. В больнице нет пациента с таким ID')
