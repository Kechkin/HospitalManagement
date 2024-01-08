from Console import Console
from UseCases import UseCases
from Hospital import Hospital
from constants import UNKNOWN_COMMAND_TRY_AGAIN, SESSION_END
from exception import ExceptionPositiveIntValue

entities = Hospital()
app = UseCases(entities)

while True:
    answer = Console.get_message('Введите команду: ')
    try:
        if answer in ['узнать статус пациента', 'get status']:
            patient_id = Console.get_message_patient_id('Введите ID пациента: ')
            app.get_status_patient(patient_id)

        elif answer in ['стоп', 'stop']:
            Console.send_message(SESSION_END)
            break

        elif answer in ['status up', 'повысить статус пациента']:
            patient_id = Console.get_message_patient_id('Введите ID пациента: ')
            app.increase_status_patient(patient_id)

        elif answer in ['status down', 'понизить статус пациента']:
            patient_id = Console.get_message_patient_id('Введите ID пациента: ')
            app.decrease_status_patient(patient_id)

        elif answer in ['discharge', 'выписать']:
            patient_id = Console.get_message_patient_id('Введите ID пациента: ')
            app.discharge_patient(patient_id)

        elif answer in ['рассчитать статистику', 'calculate statistics']:
            app.show_calculated_hospital_statistics()

        else:
            Console.send_message(UNKNOWN_COMMAND_TRY_AGAIN)

    except ExceptionPositiveIntValue as error:
        Console.send_message(error.args[0])
