from UseCases import UseCases
from Hospital import Hospital


class TestCalculateTextStatistics:
    entities = Hospital()
    app = UseCases(entities)

    def test_calculate(self):
        self.entities._list_of_patients = [1, 1, 1]
        assert self.app.show_calculated_hospital_statistics() == (
            'В больнице на данный момент находится 3 чел., из них: \n'
            '        в статусе "Болен": 3 чел. \n')

    def test_patient_with_status_zero(self):
        self.entities._list_of_patients = [0, 0, 0]
        assert self.app.show_calculated_hospital_statistics() == (
            'В больнице на данный момент находится 3 чел., из них: \n'
            '        в статусе "Тяжело болен": 3 чел. \n')

    def test_patient_with_status_three(self):
        self.entities._list_of_patients = [3, 3, 3]
        assert self.app.show_calculated_hospital_statistics(), (
            'В больнице на данный момент находится 3 чел., из них: \n'
            '        в статусе "Готов к выписке": 3 чел. \n')

    def test_patient_with_status_two(self):
        self.entities._list_of_patients = [2, 2, 2]
        assert self.app.show_calculated_hospital_statistics() == (
            'В больнице на данный момент находится 3 чел., из них: \n'
            '        в статусе "Слегка болен": 3 чел. \n')

    def test_empty_list(self):
        self.entities._list_of_patients = []
        assert self.app.show_calculated_hospital_statistics() == ('В больнице на данный момент находится 0 чел., '
                                                                  'из них: \n')

    def test_different_statuses(self):
        self.entities._list_of_patients = [0, 0, 1, 1, 2, 2, 3, 3]
        assert self.app.show_calculated_hospital_statistics() == (
            'В больнице на данный момент находится 8 чел., из них: \n'
            '        в статусе "Тяжело болен": 2 чел. \n'
            '        в статусе "Болен": 2 чел. \n'
            '        в статусе "Слегка болен": 2 чел. \n'
            '        в статусе "Готов к выписке": 2 чел. \n')


class TestCalculateValuesDataStatistic:
    entities = Hospital()
    app = UseCases(entities)

    def test_calculate_statuses(self):
        self.entities._list_of_patients = [0, 0, 1, 1, 2, 2, 3, 3]
        assert self.entities.get_calculated_statistics() == {'Болен': 2, 'Готов к выписке': 2,
                                                             'Слегка болен': 2, 'Тяжело болен': 2}

    def test_calculate_empty_list(self):
        self.entities._list_of_patients = []
        assert self.entities.get_calculated_statistics() == {'Болен': 0, 'Готов к выписке': 0,
                                                             'Слегка болен': 0, 'Тяжело болен': 0}

    def test_calculate_status_number_zero(self):
        self.entities._list_of_patients = [0, 0]
        assert self.entities.get_calculated_statistics() == {'Болен': 0, 'Готов к выписке': 0,
                                                             'Слегка болен': 0, 'Тяжело болен': 2}

    def test_calculate_status_number_one(self):
        self.entities._list_of_patients = [1, 1]
        assert self.entities.get_calculated_statistics() == {'Болен': 2, 'Готов к выписке': 0,
                                                             'Слегка болен': 0, 'Тяжело болен': 0}

    def test_calculate_status_number_two(self):
        self.entities._list_of_patients = [2, 2]
        assert self.entities.get_calculated_statistics() == {'Болен': 0, 'Готов к выписке': 0,
                                                             'Слегка болен': 2, 'Тяжело болен': 0}

    def test_calculate_status_number_three(self):
        self.entities._list_of_patients = [3, 3]
        assert self.entities.get_calculated_statistics() == {'Болен': 0, 'Готов к выписке': 2,
                                                             'Слегка болен': 0, 'Тяжело болен': 0}

    def test_calculate_status_where_text_instead_number(self):
        self.entities._list_of_patients = ['text', 2]
        assert self.entities.get_calculated_statistics() == {'Болен': 0, 'Готов к выписке': 0,
                                                             'Слегка болен': 1, 'Тяжело болен': 0}

    def test_calculate_status_where_number_below_zero(self):
        self.entities._list_of_patients = [-12, 2]
        assert self.entities.get_calculated_statistics() == {'Болен': 0, 'Готов к выписке': 0,
                                                             'Слегка болен': 1, 'Тяжело болен': 0}
