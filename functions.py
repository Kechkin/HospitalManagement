from constants import (DEFAULT_COUNT_PATIENTS, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)


def generate_patients_with_statuses_from_zero_to_three(count: int = DEFAULT_COUNT_PATIENTS, status: int = 1):
    return [status for _ in range(count)]


def validate_input_value_from_client(patient_id):
    if patient_id.isdigit():
        return int(patient_id)
    else:
        print(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
