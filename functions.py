from constants import (DEFAULT_COUNT_PATIENTS, ZERO, ONE, TWO, THREE, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)


def generate_patients_with_statuses(count: int = DEFAULT_COUNT_PATIENTS, status: int = 1):
    # status should be from 0 to 3
    return [status for _ in range(count)]


def get_calculated_results(data):
    data_for_calculate_status = {
        'Тяжело болен': data.count(ZERO),
        'Болен': data.count(ONE),
        'Слегка болен': data.count(TWO),
        'Готов к выписке': data.count(THREE),
    }
    result = f'В больнице на данный момент находится {len(data)} чел., из них: \n'
    for k, v in data_for_calculate_status.items():
        if v != ZERO:
            result += f'        в статусе "{k}": {v} чел. \n'
    return result


def validate_input(patient_id):
    if patient_id.isdigit():
        return int(patient_id)
    else:
        print(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
