from constants import (DEFAULT_COUNT_PATIENTS, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
from exception import ExceptionPositiveIntValue


def generate_patients_with_statuses_from_zero_to_three(count: int = DEFAULT_COUNT_PATIENTS, status: int = 1):
    return [status for _ in range(count)]


def validate_patient_id_from_input(patient_id):
    if not patient_id.isdigit():
        raise ExceptionPositiveIntValue(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
    return int(patient_id)
