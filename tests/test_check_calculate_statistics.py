from HospitalApp import Hospital
from Service import BaseLogic
from functions import generate_patients_with_statuses


class TestCalculateStatistics:
    service = BaseLogic()
    app = Hospital(service)

    def test_calculate(self):
        self.service._list_of_patients = [1, 1, 1, 1, 1]
        assert self.app.calculate_statistics() == ('В больнице на данный момент находится 5 чел., из них: \n'
                                                   '        в статусе "Болен": 5 чел. \n')

    def test_patient_with_status_zero(self):
        self.service._list_of_patients = generate_patients_with_statuses(5, 0)
        assert self.app.calculate_statistics() == ('В больнице на данный момент находится 5 чел., из них: \n'
                                                   '        в статусе "Тяжело болен": 5 чел. \n')

    def test_patient_with_status_three(self):
        self.service._list_of_patients = generate_patients_with_statuses(5, 3)
        assert self.app.calculate_statistics(), ('В больнице на данный момент находится 5 чел., из них: \n'
                                                 '        в статусе "Готов к выписке": 5 чел. \n')

    def test_patient_with_status_two(self):
        self.service._list_of_patients = generate_patients_with_statuses(5, 2)
        assert self.app.calculate_statistics() == ('В больнице на данный момент находится 5 чел., из них: \n'
                                                   '        в статусе "Слегка болен": 5 чел. \n')

    def test_empty_list(self):
        self.service._list_of_patients = generate_patients_with_statuses(0, 2)
        assert self.app.calculate_statistics() == ('В больнице на данный момент находится 0 чел., '
                                                   'из них: \n')

    def test_different_statuses(self):
        self.service._list_of_patients = [1, 3, 1, 1, 1, 1, 0, 0, 2, 2, 2, 3, 3, 1, 1, 2, 2, 3, 0, 0]
        assert self.app.calculate_statistics() == (
            'В больнице на данный момент находится 20 чел., из них: \n'
            '        в статусе "Тяжело болен": 4 чел. \n'
            '        в статусе "Болен": 7 чел. \n'
            '        в статусе "Слегка болен": 5 чел. \n'
            '        в статусе "Готов к выписке": 4 чел. \n')

    def test_stop(self):
        assert self.app.stop(), 'Сеанс завершён.'
