from DialogueWithTheUser import DialogueWithTheUser
from UseCases import UseCases
from Hospital import Hospital
from exception import ExceptionPositiveIntValue

entities = Hospital()
dialog = DialogueWithTheUser()
app = UseCases(entities, dialog)

while True:
    answer = dialog.get_entered_command_message_from_user()
    try:
        if answer in ['узнать статус пациента', 'get status']:
            patient_id = dialog.get_patient_id()
            app.get_patient_status(patient_id)

        elif answer in ['стоп', 'stop']:
            dialog.send_message('Сеанс завершён.')
            break

        elif answer in ['status up', 'повысить статус пациента']:
            patient_id = dialog.get_patient_id()
            app.increase_patient_status(patient_id)

        elif answer in ['status down', 'понизить статус пациента']:
            patient_id = dialog.get_patient_id()
            app.decrease_patient_status(patient_id)

        elif answer in ['discharge', 'выписать']:
            patient_id = dialog.get_patient_id()
            app.discharge_patient(patient_id)

        elif answer in ['рассчитать статистику', 'calculate statistics']:
            app.show_calculated_statistics()

        else:
            dialog.send_message('Неизвестная команда! Попробуйте ещё раз')

    except ExceptionPositiveIntValue as error:
        dialog.send_message(error.args[0])
