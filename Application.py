from DialogWithUser import DialogWithUser
from Hospital import Hospital
from UseCases import UseCases
from console import Console
from exception import ExceptionPositiveIntValue


class Application:
    dialog_with_user = None
    commands = None

    def __init__(self, dialog_with_user, commands):
        self.dialog_with_user = dialog_with_user
        self.commands = commands

    def main(self):
        while True:
            answer = self.dialog_with_user.get_entered_command_message_from_user()
            try:
                if answer in ['узнать статус пациента', 'get status']:
                    patient_id = self.dialog_with_user.get_patient_id()
                    self.commands.get_patient_status(patient_id)

                elif answer in ['стоп', 'stop']:
                    self.dialog_with_user.send_message('Сеанс завершён.')
                    break

                elif answer in ['status up', 'повысить статус пациента']:
                    patient_id = self.dialog_with_user.get_patient_id()
                    self.commands.increase_patient_status(patient_id)

                elif answer in ['status down', 'понизить статус пациента']:
                    patient_id = self.dialog_with_user.get_patient_id()
                    self.commands.decrease_patient_status(patient_id)

                elif answer in ['discharge', 'выписать']:
                    patient_id = self.dialog_with_user.get_patient_id()
                    self.commands.discharge_patient(patient_id)

                elif answer in ['рассчитать статистику', 'calculate statistics']:
                    self.commands.show_calculated_statistics()

                else:
                    self.dialog_with_user.send_message('Неизвестная команда! Попробуйте ещё раз')

            except ExceptionPositiveIntValue as error:
                self.dialog_with_user.send_message(error.args[0])


if __name__ == "__main__":
    console = Console()
    entities = Hospital()
    dialog_with_user = DialogWithUser(console)
    commands = UseCases(entities, dialog_with_user)
    app = Application(dialog_with_user, commands)
    app.main()
