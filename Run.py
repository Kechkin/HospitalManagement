from UseCases import UseCases
from Hospital import Hospital
from constants import UNKNOWN_COMMAND_TRY_AGAIN, SESSION_END
from exception import ExceptionPositiveIntValue
from functions import validate_patient_id_from_input

entities = Hospital()
app = UseCases(entities)

while True:
    answer = input('Введите команду: ')
    try:
        if answer in ['узнать статус пациента', 'get status']:
            patient_id = input('Введите ID пациента: ')
            validate_patient_id_from_input(patient_id)
            print(app.get_status_patient(int(patient_id)))

        elif answer in ['стоп', 'stop']:
            print(SESSION_END)
            break

        elif answer in ['status up', 'повысить статус пациента']:
            patient_id = input('Введите ID пациента: ')
            validate_patient_id_from_input(patient_id)
            print(app.get_increase_new_status_patient(int(patient_id)))

        elif answer in ['status down', 'понизить статус пациента']:
            patient_id = input('Введите ID пациента: ')
            validate_patient_id_from_input(patient_id)
            print(app.get_decrease_new_status_patient(int(patient_id)))

        elif answer in ['discharge', 'выписать']:
            patient_id = input('Введите ID пациента: ')
            validate_patient_id_from_input(patient_id)
            print(app.get_discharge_patient_status(int(patient_id)))

        elif answer in ['рассчитать статистику', 'calculate statistics']:
            print(app.show_calculated_hospital_statistics())

        else:
            print(UNKNOWN_COMMAND_TRY_AGAIN)

    except ExceptionPositiveIntValue as error:
        print(error.args[0])
