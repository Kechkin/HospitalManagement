import pytest

from DialogueWithTheUser import DialogueWithTheUser
from exception import ExceptionPositiveIntValue


class TestConvertedTextToPatientIDValue:
    def test_convert_text_to_patient_id(self):
        assert DialogueWithTheUser._get_converted_text_to_patient_id_value(patient_id_as_text='123') == 123

    def test_convert_text_to_patient_id_when_its_not_int(self):
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_converted_text_to_patient_id_value(patient_id_as_text='two')

    def test_convert_text_to_patient_id_when_its_empty(self):
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_converted_text_to_patient_id_value(patient_id_as_text='')

    def test_convert_text_to_patient_id_when_its_not_positive(self):
        with pytest.raises(ExceptionPositiveIntValue):
            DialogueWithTheUser._get_converted_text_to_patient_id_value(patient_id_as_text='-123')
