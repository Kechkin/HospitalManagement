def generate_patients_with_statuses_from_zero_to_three(count: int = 200, status: int = 1):
    # сгенерировать количество пациентов со статусами от нуля до трёх
    return [status for _ in range(count)]
