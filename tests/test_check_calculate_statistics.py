from DialogWithUser import DialogWithUser
from UseCases import UseCases
from Hospital import Hospital


class TestCalculateTextStatistics:
    entities = Hospital()
    dialog = DialogWithUser()
    app = UseCases(entities, dialog)

    def test_for_converting_calculated_statistics_into_text(self):
        count_of_patients = 3
        data_calculated_statistics = {'Тяжело болен': 0,
                                      'Болен': 3,
                                      'Слегка болен': 0,
                                      'Готов к выписке': 0}

        assert self.app._convert_calculated_statistics_to_text(data_calculated_statistics, count_of_patients) == (
            'В больнице на данный момент находится 3 чел., из них: \n'
            '        в статусе "Болен": 3 чел. \n')

    def test_for_converting_calculated_statistics_into_text_when_list_is_empty(self):
        count_of_patients = 0
        data_calculated_statistics = {'Тяжело болен': 0,
                                      'Болен': 0,
                                      'Слегка болен': 0,
                                      'Готов к выписке': 0}
        assert self.app._convert_calculated_statistics_to_text(data_calculated_statistics, count_of_patients) == (
            'В больнице на данный момент находится 0 чел., '
            'из них: \n')

    def test_for_converting_calculated_statistics_into_text_with_different_values_in_statuses(self):
        count_of_patients = 8
        data_calculated_statistics = {'Тяжело болен': 1,
                                      'Болен': 3,
                                      'Слегка болен': 2,
                                      'Готов к выписке': 1}

        assert self.app._convert_calculated_statistics_to_text(data_calculated_statistics, count_of_patients) == (
            'В больнице на данный момент находится 8 чел., из них: \n'
            '        в статусе "Тяжело болен": 1 чел. \n'
            '        в статусе "Болен": 3 чел. \n'
            '        в статусе "Слегка болен": 2 чел. \n'
            '        в статусе "Готов к выписке": 1 чел. \n')

        data_calculated_statistics = {'Тяжело болен': 0,
                                      'Болен': 1,
                                      'Слегка болен': 3,
                                      'Готов к выписке': 2}

        assert self.app._convert_calculated_statistics_to_text(data_calculated_statistics, count_of_patients) == (
            'В больнице на данный момент находится 8 чел., из них: \n'
            '        в статусе "Болен": 1 чел. \n'
            '        в статусе "Слегка болен": 3 чел. \n'
            '        в статусе "Готов к выписке": 2 чел. \n')


class TestCalculateValuesDataStatistic:
    entities = Hospital()
    dialog = DialogWithUser()
    app = UseCases(entities, dialog)

    def test_statistics_calculation(self):
        self.entities._list_of_patients = [0, 1, 1, 1, 2, 2, 3, 3]
        assert self.entities.get_calculated_statistics() == {'Болен': 3, 'Готов к выписке': 2,
                                                             'Слегка болен': 2, 'Тяжело болен': 1}

    def test_statistics_calculation_when_list_is_empty(self):
        self.entities._list_of_patients = []
        assert self.entities.get_calculated_statistics() == {'Болен': 0, 'Готов к выписке': 0,
                                                             'Слегка болен': 0, 'Тяжело болен': 0}

    def test_statistics_calculation_with_one_status(self):
        self.entities._list_of_patients = [1, 1]
        assert self.entities.get_calculated_statistics() == {'Болен': 2, 'Готов к выписке': 0,
                                                             'Слегка болен': 0, 'Тяжело болен': 0}
