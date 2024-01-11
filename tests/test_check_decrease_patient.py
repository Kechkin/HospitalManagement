from unittest.mock import MagicMock

from DialogueWithTheUser import DialogueWithTheUser
from UseCases import UseCases
from Hospital import Hospital


class TestDecreasePatient:
    entities = Hospital()
    dialog = DialogueWithTheUser()
    app = UseCases(entities, dialog)

    def test_for_decrease_patient_status(self):
        self.entities._list_of_patients = [2, 1, 2]
        self.dialog.send_message = MagicMock()
        self.app.decrease_patient_status(2)
        self.dialog.send_message('Новый статус пациента: Тяжело болен')
        self.dialog.send_message.assert_called_with('Новый статус пациента: Тяжело болен')
        assert self.entities._list_of_patients == [2, 0, 2]

    def test_where_patient_id_is_out_of_range_the_list(self):
        self.dialog.send_message = MagicMock()
        self.app.decrease_patient_status(224)
        self.dialog.send_message.assert_called_with('Ошибка. В больнице нет пациента с таким ID')

    def test_for_decrease_from_highest_status_to_lowest(self):
        self.entities._list_of_patients = [3, 2, 3, 2, 3]
        self.dialog.send_message = MagicMock()
        self.app.decrease_patient_status(5)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Слегка болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 2]

        self.app.decrease_patient_status(5)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 1]

        self.app.decrease_patient_status(5)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Тяжело болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 0]

    def test_to_decrease_the_lowest_status(self):
        self.entities._list_of_patients = [3, 2, 0]
        self.dialog.send_message = MagicMock()
        self.app.decrease_patient_status(3)
        self.dialog.send_message.assert_called_with(
            'Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)'
        )


class TestCanDecreaseStatus:
    entities = Hospital()
    dialog = DialogueWithTheUser()
    app = UseCases(entities, dialog)

    def test_if_not_allowed_decrease_status_then_get_false(self):
        self.entities._list_of_patients = [0, 2, 1]
        assert self.entities.approve_to_decrease_status(patient_id=1) is False

    def test_if_allowed_decrease_status_then_get_true(self):
        self.entities._list_of_patients = [3, 1, 2]
        assert self.entities.approve_to_decrease_status(patient_id=1) is True
