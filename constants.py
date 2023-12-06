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

ERROR_INT: str = 'Ошибка. ID пациента должно быть числом (целым, положительным)'
ERROR_DECREASE: str = 'Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)'
NOT_FOUND: str = 'Ошибка. В больнице нет пациента с таким ID'
TRY_AGAIN: str = 'Неизвестная команда! Попробуйте ещё раз'
PATIENT_READY: str = 'Пациент остался в статусе "Готов к выписке"'
PATIENT_DONE: str = 'Пациент выписан из больницы'
YES: str = 'да'
SESSION_END: str = 'Сеанс завершён.'
