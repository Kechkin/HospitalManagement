import pytest

from DialogueWithTheUser import DialogueWithTheUser
from exception import ExceptionPositiveIntValue


class TestConvertedTextToPatientIDValue:

    def test_convert_text_to_patient_id(self):
        # тест, в котором число в виде текста преобразуется в положительное числовое значение
        # test_where_number_as_text_is_converted_to_positive_numbers_value
        assert DialogueWithTheUser._get_converted_text_to_patient_id_value(patient_id_as_text='123') == 123

    def test_convert_text_to_patient_id_when_its_not_int(self):
        # тест, в котором текст из слов не может быть преобразован в число
        # test_where_text_of_words_cannot_be_converted_to_number
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_converted_text_to_patient_id_value(patient_id_as_text='two')

    def test_convert_text_to_patient_id_when_its_empty(self):
        # тест, в котором пустое значение не может быть преобразовано в число
        # test_where_empty_text_cannot_be_converted_to_number
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_converted_text_to_patient_id_value(patient_id_as_text='')

    def test_convert_text_to_patient_id_when_its_not_positive(self):
        # тест, в котором отрицательное число в виде текста не может быть преобразован в число
        # test_where_negative_number_as_text_cannot_be_converted_to_number
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_converted_text_to_patient_id_value(patient_id_as_text='-123')
