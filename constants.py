ZERO: int = 0
ONE: int = 1
TWO: int = 2
THREE: int = 3
DEFAULT_COUNT_PATIENTS: int = 200

PATIENT_STATUSES: dict = {
    0: 'Тяжело болен',
    1: 'Болен',
    2: 'Слегка болен',
    3: 'Готов к выписке'
}

ERROR_VALUE_SHOULD_BE_UNSIGNED_INT: str = 'Ошибка. ID пациента должно быть числом (целым, положительным)'
ERROR_CANNOT_DECREASE_LOW_STATUS: str = 'Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)'
ERROR_THERE_IS_NOT_PATIENT_WITH_THIS_ID: str = 'Ошибка. В больнице нет пациента с таким ID'
UNKNOWN_COMMAND_TRY_AGAIN: str = 'Неизвестная команда! Попробуйте ещё раз'
PATIENT_STATUS_READY_TO_DISCHARGE: str = 'Пациент остался в статусе "Готов к выписке"'
PATIENT_DISCHARGED: str = 'Пациент выписан из больницы'
ERROR_THERE_IS_NO_PATIENT_ID: str = 'Ошибка. Такого пациента нет'
ERROR_INPUT_UNSIGNED_INT: str = 'Ошибка. Вводите число'
ERROR_EMPTY_VALUE_INPUT_UNSIGNED_INT: str = 'Ошибка. Пустое значение, введите число'

YES: str = 'да'
NO: str = 'нет'
TEXT: str = 'text'
SESSION_END: str = 'Сеанс завершён.'
