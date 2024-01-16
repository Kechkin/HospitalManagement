from unittest.mock import MagicMock

from DialogWithUser import DialogWithUser
from UseCases import UseCases
from Hospital import Hospital


class TestDischarge:
    entities = Hospital()
    dialog = DialogWithUser()
    app = UseCases(entities, dialog)

    def test_patient_discharge(self):
        self.entities._list_of_patients = [1, 2, 1]
        self.dialog.send_message = MagicMock()
        self.app.discharge_patient(3)
        self.dialog.send_message.assert_called_with('Пациент выписан из больницы')
        assert self.entities._list_of_patients == [1, 2]

    def test_cannot_discharge_patient_when_list_is_empty(self):
        self.entities._list_of_patients = [1, 2, 1]
        self.dialog.send_message = MagicMock()
        self.app.discharge_patient(100)
        self.dialog.send_message.assert_called_with('Ошибка. В больнице нет пациента с таким ID')

    def test_cannot_discharge_patient_when_id_is_outside_list(self):
        self.entities._list_of_patients = [3, 3, 3]
        self.dialog.send_message = MagicMock()
        self.app.discharge_patient(300)
        self.dialog.send_message.assert_called_with('Ошибка. В больнице нет пациента с таким ID')
