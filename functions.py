from constants import (DEFAULT_COUNT_PATIENTS)


def generate_patients_with_statuses_from_zero_to_three(count: int = DEFAULT_COUNT_PATIENTS, status: int = 1):
    return [status for _ in range(count)]
