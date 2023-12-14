from constants import ERROR_INPUT_UNSIGNED_INT, ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
from functions import check_patient_id


class FunctionForDecorator:
    _variable = 0

    @check_patient_id
    def victim_test(self, patient_id):
        self._variable = 10
        return f'функция вернула значение: {patient_id}'

    @property
    def variable(self):
        result = self._variable
        self._variable = 0
        return result


class TestCheckDischarge:
    test_func = FunctionForDecorator()

    def test_run_func(self):
        patient_id = 15
        assert self.test_func.victim_test(15) == f'функция вернула значение: {patient_id}'
        # Check that func run and change variable
        assert self.test_func.variable == 10

    def test_validate_text(self):
        assert self.test_func.victim_test('text') == ERROR_INPUT_UNSIGNED_INT
        # Check that func didn't run and didn't change variable
        assert self.test_func.variable == 0

    def test_validate_empty_value(self):
        assert self.test_func.victim_test(None) == ERROR_INPUT_UNSIGNED_INT
        assert self.test_func.victim_test('') == ERROR_INPUT_UNSIGNED_INT
        # With empty () in decorator args is empty value in tuple
        assert self.test_func.victim_test() == ERROR_INPUT_UNSIGNED_INT
        # Check that func didn't run and didn't change variable
        assert self.test_func.variable == 0

    def test_validate_max_mix_value(self):
        assert self.test_func.victim_test(214) == ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
        assert self.test_func.victim_test(-14) == ERROR_INPUT_UNSIGNED_INT
        # Check that func didn't run and didn't change variable
        assert self.test_func.variable == 0
