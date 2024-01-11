from unittest.mock import MagicMock

from DialogueWithTheUser import DialogueWithTheUser
from UseCases import UseCases
from Hospital import Hospital


class TestDecreasePatient:
    entities = Hospital()
    dialog = DialogueWithTheUser()
    app = UseCases(entities, dialog)

    def test_decrease_patient(self):
        # тест на понижение статуса пациента
        # test_for_decrease_patient_status
        self.entities._list_of_patients = [2, 1, 2]
        self.dialog.send_message = MagicMock()
        self.app.decrease_status_patient(2)
        self.dialog.send_message('Новый статус пациента: Тяжело болен')
        self.dialog.send_message.assert_called_with('Новый статус пациента: Тяжело болен')
        assert self.entities._list_of_patients == [2, 0, 2]

    def test_max_id(self):
        # тест, в котором айди пациента выходит за пределы списка
        # test_where_patient_id_is_out_of_range_the_list
        self.dialog.send_message = MagicMock()
        self.app.decrease_status_patient(224)
        self.dialog.send_message.assert_called_with('Ошибка. В больнице нет пациента с таким ID')

    def test_decrease_from_max_to_min_status(self):
        # тест на снижение от самого высокого статуса до самого низкого
        # test_for_decrease_from_highest_status_to_lowest
        self.entities._list_of_patients = [3, 2, 3, 2, 3]
        self.dialog.send_message = MagicMock()
        self.app.decrease_status_patient(5)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Слегка болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 2]

        self.app.decrease_status_patient(5)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 1]

        self.app.decrease_status_patient(5)
        self.dialog.send_message.assert_called_with('Новый статус пациента: Тяжело болен')
        assert self.entities._list_of_patients == [3, 2, 3, 2, 0]

    def test_max_decrease(self):
        # тест на понижение самого низкого статуса
        # test_to_decrease_the_lowest_status

        self.entities._list_of_patients = [3, 2, 0]
        self.dialog.send_message = MagicMock()
        self.app.decrease_status_patient(3)
        self.dialog.send_message.assert_called_with(
            'Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)'
        )


class TestCanDecreaseStatus:
    entities = Hospital()
    dialog = DialogueWithTheUser()
    app = UseCases(entities, dialog)

    def test_can_not_decrease_status_patient_id_get_false(self):
        # тест если запрещено понижать статус тогда верни false
        # test_if_not_allowed_decrease_status_then_get_false

        self.entities._list_of_patients = [0, 2, 1]
        assert self.entities.can_decrease_status_patient(patient_id=1) is False

    def test_can_increase_status_get_true(self):
        # тест, если разрешено уменьшать статус, тогда верни true
        # test_if_allowed_decrease_status_then_get_true
        self.entities._list_of_patients = [3, 1, 2]
        assert self.entities.can_decrease_status_patient(patient_id=1) is True
