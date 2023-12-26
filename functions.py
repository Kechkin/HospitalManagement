from constants import (DEFAULT_COUNT_PATIENTS, ZERO, ERROR_VALUE_SHOULD_BE_UNSIGNED_INT,
                       ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID)


def generate_patients_with_statuses_from_zero_to_three(count: int = DEFAULT_COUNT_PATIENTS, status: int = 1):
    return [status for _ in range(count)]


def validate_patient_id(patient_id, patients_list):
    if not isinstance(patient_id, int) or patient_id <= ZERO:
        return ERROR_VALUE_SHOULD_BE_UNSIGNED_INT
    elif patient_id > len(patients_list):
        return ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID


def validate_input_value_from_client(patient_id):
    if patient_id.isdigit():
        return int(patient_id)
    else:
        print(ERROR_VALUE_SHOULD_BE_UNSIGNED_INT)
