from constants import DEFAULT_COUNT_PATIENTS, ZERO, ONE, TWO, THREE


def generate_patients(count: int = DEFAULT_COUNT_PATIENTS):
    return [1 for _ in range(count)]


def show_calculated_results(data):
    data_for_calculate_status = {
        'Тяжело болен': data.count(ZERO),
        'Болен': data.count(ONE),
        'Слегка болен': data.count(TWO),
        'Готов к выписке': data.count(THREE),
    }
    result = f'В больнице на данный момент находится {len(data)} чел., из них: \n'
    for k, v in data_for_calculate_status.items():
        if v != ZERO:
            result += f'в статусе "{k}": {v} чел. \n'
    return result
