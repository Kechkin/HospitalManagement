from constants import DEFAULT_COUNT_PATIENTS, ZERO, ONE, TWO, THREE, ERROR_VALUE_INTEGER, PATIENT_NOT_FOUND, \
    ERROR_INPUT_INT, ERROR_EMPTY_VALUE


def generate_patients(count: int = DEFAULT_COUNT_PATIENTS, status: int = 1):
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


# Тест сделать
def check_patient_id(func):
    def inner(*args, **kwargs):
        if len(args) >= 2:
            patient_id = args[1]
            if not isinstance(patient_id, int):
                return ERROR_INPUT_INT
            if patient_id > DEFAULT_COUNT_PATIENTS or patient_id <= ZERO:
                return PATIENT_NOT_FOUND
            else:
                return func(*args, **kwargs)
        else:
            return ERROR_EMPTY_VALUE
    return inner


def validate_input(patient_id):
    if patient_id.isdigit():
        return int(patient_id)
    else:
        print(ERROR_VALUE_INTEGER)
