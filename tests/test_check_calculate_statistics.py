from UseCases import UseCases
from Hospital import Hospital
from functions import generate_patients_with_statuses_from_zero_to_three


class TestCalculateStatistics:
    service = Hospital()
    app = UseCases(service)

    def test_calculate(self):
        self.service._list_of_patients = [1, 1, 1, 1, 1]
        assert self.app.show_calculated_statistics() == ('В больнице на данный момент находится 5 чел., из них: \n'
                                                         '        в статусе "Болен": 5 чел. \n')

    def test_patient_with_status_zero(self):
        self.service._list_of_patients = generate_patients_with_statuses_from_zero_to_three(5, 0)
        assert self.app.show_calculated_statistics() == ('В больнице на данный момент находится 5 чел., из них: \n'
                                                         '        в статусе "Тяжело болен": 5 чел. \n')

    def test_patient_with_status_three(self):
        self.service._list_of_patients = generate_patients_with_statuses_from_zero_to_three(5, 3)
        assert self.app.show_calculated_statistics(), ('В больнице на данный момент находится 5 чел., из них: \n'
                                                       '        в статусе "Готов к выписке": 5 чел. \n')

    def test_patient_with_status_two(self):
        self.service._list_of_patients = generate_patients_with_statuses_from_zero_to_three(5, 2)
        assert self.app.show_calculated_statistics() == ('В больнице на данный момент находится 5 чел., из них: \n'
                                                         '        в статусе "Слегка болен": 5 чел. \n')

    def test_empty_list(self):
        self.service._list_of_patients = generate_patients_with_statuses_from_zero_to_three(0, 2)
        assert self.app.show_calculated_statistics() == ('В больнице на данный момент находится 0 чел., '
                                                         'из них: \n')

    def test_different_statuses(self):
        self.service._list_of_patients = [1, 3, 1, 1, 1, 1, 0, 0, 2, 2, 2, 3, 3, 1, 1, 2, 2, 3, 0, 0]
        assert self.app.show_calculated_statistics() == (
            'В больнице на данный момент находится 20 чел., из них: \n'
            '        в статусе "Тяжело болен": 4 чел. \n'
            '        в статусе "Болен": 7 чел. \n'
            '        в статусе "Слегка болен": 5 чел. \n'
            '        в статусе "Готов к выписке": 4 чел. \n')
