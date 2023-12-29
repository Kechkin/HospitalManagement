from UseCases import UseCases
from Hospital import Hospital
from constants import UNKNOWN_COMMAND_TRY_AGAIN, SESSION_END
from functions import validate_input_value_from_client

entities = Hospital()
app = UseCases(entities)

while True:
    answer = input('Введите команду: ')

    if answer in ['узнать статус пациента', 'get status']:
        patient_id = input('Введите ID пациента: ')
        patient_id_validated = validate_input_value_from_client(patient_id)
        if patient_id_validated:
            print(app.get_status_patient(patient_id_validated))

    elif answer in ['стоп', 'stop']:
        print(SESSION_END)
        break

    elif answer in ['status up', 'повысить статус пациента']:
        patient_id = input('Введите ID пациента: ')
        patient_id_validated = validate_input_value_from_client(patient_id)
        if patient_id_validated:
            print(app.increase_status_patient(patient_id_validated))

    elif answer in ['status down', 'понизить статус пациента']:
        patient_id = input('Введите ID пациента: ')
        patient_id_validated = validate_input_value_from_client(patient_id)
        if patient_id_validated:
            print(app.decrease_status_patient(patient_id_validated))

    elif answer in ['discharge', 'выписать']:
        patient_id = input('Введите ID пациента: ')
        patient_id_validated = validate_input_value_from_client(patient_id)
        if patient_id_validated:
            print(app.discharge_patient(patient_id_validated))

    elif answer in ['рассчитать статистику', 'calculate statistics']:
        print(app.show_calculated_hospital_statistics())

    else:
        print(UNKNOWN_COMMAND_TRY_AGAIN)
