from constants import (DEFAULT_COUNT_PATIENTS, ZERO, ONE, TWO, THREE, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT,
                       ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID, ERROR_INPUT_UNSIGNED_INT)


def generate_patients_with_statuses(count: int = DEFAULT_COUNT_PATIENTS, status: int = 1):
    return [status for _ in range(count)]


def get_calculated_results(data):
    data_for_calculate_status = {
        'Тяжело болен': data.count(ZERO),
        'Болен': data.count(ONE),
        'Слегка болен': data.count(TWO),
        'Готов к выписке': data.count(THREE),
    }
    result = f'В больнице на данный момент находится {len(data)} чел., из них: '
    for k, v in data_for_calculate_status.items():
        if v != ZERO:
            result += f'в статусе "{k}": {v} чел.'
    return result


def check_patient_id(func):
    def inner(*args, **kwargs):
        if len(args) >= 2:
            patient_id = args[1]
            if not isinstance(patient_id, int) or patient_id <= ZERO:
                return ERROR_INPUT_UNSIGNED_INT
            elif patient_id > DEFAULT_COUNT_PATIENTS:
                return ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID
            else:
                return func(*args, **kwargs)
        else:
            return ERROR_INPUT_UNSIGNED_INT
    return inner


def validate_input(patient_id):
    if patient_id.isdigit():
        return int(patient_id)
    else:
        print(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
