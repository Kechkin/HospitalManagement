from Hospital import Hospital
from constants import TRY_AGAIN
from functions import validate_input

app = Hospital()

while True:
    answer = input('Введите команду: ')

    if answer in ['узнать статус пациента', 'get status']:
        patient_id = input('Введите ID пациента: ')
        patient_id_validated = validate_input(patient_id)
        if patient_id_validated:
            print(app.get_status_patient(patient_id_validated))

    elif answer in ['стоп', 'stop']:
        print(app.stop())
        break

    elif answer in ['status up', 'повысить статус пациента']:
        patient_id = input('Введите ID пациента: ')
        patient_id_validated = validate_input(patient_id)
        if patient_id_validated:
            print(app.increase_status_patient(patient_id_validated))

    elif answer in ['status down', 'понизить статус пациента']:
        patient_id = input('Введите ID пациента: ')
        patient_id_validated = validate_input(patient_id)
        if patient_id_validated:
            print(app.decrease_status_patient(patient_id_validated))

    elif answer in ['discharge', 'выписать']:
        patient_id = input('Введите ID пациента: ')
        patient_id_validated = validate_input(patient_id)
        if patient_id_validated:
            print(app.discharge_patient(patient_id_validated))

    elif answer in ['рассчитать статистику', 'calculate statistics']:
        print(app.calculate_statistics())

    else:
        print(TRY_AGAIN)
