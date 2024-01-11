from unittest.mock import MagicMock

from DialogueWithTheUser import DialogueWithTheUser
from UseCases import UseCases
from Hospital import Hospital


class TestGetPatientStatus:
    entities = Hospital()
    dialog = DialogueWithTheUser()
    app = UseCases(entities, dialog)

    def test_patient_status(self):
        # тест на получение статуса пациента
        # test_patient_status
        self.entities._list_of_patients = [2, 2, 2, 2]
        self.dialog.send_message = MagicMock()
        self.app.get_status_patient(4)
        self.dialog.send_message.assert_called_with('Статус пациента: Слегка болен')

    def test_different_statuses(self):
        # тест на получение разных статусов пациента
        # test_to_get_different_patient_statuses
        self.entities._list_of_patients = [3, 3, 3]
        self.dialog.send_message = MagicMock()
        self.app.get_status_patient(2)
        self.dialog.send_message.assert_called_with('Статус пациента: Готов к выписке')

        self.entities._list_of_patients = [3, 2, 3]
        self.app.get_status_patient(2)
        self.dialog.send_message.assert_called_with('Статус пациента: Слегка болен')

        self.entities._list_of_patients = [3, 1, 3]
        self.app.get_status_patient(2)
        self.dialog.send_message.assert_called_with('Статус пациента: Болен')

        self.entities._list_of_patients = [3, 0, 3]
        self.app.get_status_patient(2)
        self.dialog.send_message.assert_called_with('Статус пациента: Тяжело болен')

    def test_error_values(self):
        # тест на то, что нельзя получить статус когда ид пациента за пределами списка
        # test_cannot_get_status_when_patient_id_is_outside_list
        self.entities._list_of_patients = [3, 3, 2]
        self.dialog.send_message = MagicMock()
        self.app.get_status_patient(11)
        self.dialog.send_message.assert_called_with('Ошибка. В больнице нет пациента с таким ID')
