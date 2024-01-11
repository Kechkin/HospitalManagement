import pytest

from DialogueWithTheUser import DialogueWithTheUser
from exception import ExceptionPositiveIntValue


class TestConvertedTextToPatientIDValue:

    def test_where_number_as_text_is_converted_to_positive_numbers_value(self):
        assert DialogueWithTheUser._get_patient_id_number_from_converted_text(patient_id_as_text='123') == 123

    def test_where_text_of_words_cannot_be_converted_to_number(self):
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_patient_id_number_from_converted_text(patient_id_as_text='two')

    def test_where_empty_text_cannot_be_converted_to_number(self):
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_patient_id_number_from_converted_text(patient_id_as_text='')

    def test_where_negative_number_as_text_cannot_be_converted_to_number(self):
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_patient_id_number_from_converted_text(patient_id_as_text='-123')
