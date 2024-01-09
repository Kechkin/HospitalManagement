from DialogueWithTheUser import DialogueWithTheUser
from UseCases import UseCases
from Hospital import Hospital
from constants import UNKNOWN_COMMAND_TRY_AGAIN, SESSION_END
from exception import ExceptionPositiveIntValue

entities = Hospital()
app = UseCases(entities)
dialog = DialogueWithTheUser()

while True:
    answer = dialog.get_message()
    try:
        if answer in ['узнать статус пациента', 'get status']:
            patient_id = dialog.get_patient_id()
            app.get_status_patient(patient_id)

        elif answer in ['стоп', 'stop']:
            dialog.send_message(SESSION_END)
            break

        elif answer in ['status up', 'повысить статус пациента']:
            patient_id = dialog.get_patient_id()
            app.increase_status_patient(patient_id)

        elif answer in ['status down', 'понизить статус пациента']:
            patient_id = dialog.get_patient_id()
            app.decrease_status_patient(patient_id)

        elif answer in ['discharge', 'выписать']:
            patient_id = dialog.get_patient_id()
            app.discharge_patient(patient_id)

        elif answer in ['рассчитать статистику', 'calculate statistics']:
            app.show_calculated_hospital_statistics()

        else:
            dialog.send_message(UNKNOWN_COMMAND_TRY_AGAIN)

    except ExceptionPositiveIntValue as error:
        dialog.send_message(error.args[0])
