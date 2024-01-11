from exception import ExceptionNoPatientInHospital


class UseCases:
    ent = None
    dialog = None

    def __init__(self, entities, dialog):
        self.ent = entities
        self.dialog = dialog

    def get_patient_status(self, patient_id: int):
        try:
            status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
            self.dialog.send_message(f'Статус пациента: {status_name}')
        except ExceptionNoPatientInHospital as error:
            self.dialog.send_message(error.args[0])

    def increase_patient_status(self, patient_id: int):
        try:
            if not self.ent.approve_to_increase_of_status(patient_id=patient_id):
                if self.dialog.request_confirmation_for_patient_discharge():
                    self.ent.discharge(patient_id=patient_id)
                    self.dialog.send_message('Пациент выписан из больницы')
                else:
                    patients_status = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
                    self.dialog.send_message(f'Пациент остался в статусе "{patients_status}"')
            else:
                self.ent.increase_status(patient_id=patient_id)
                patients_status = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
                self.dialog.send_message(f'Новый статус пациента: {patients_status}')
        except ExceptionNoPatientInHospital as error:
            self.dialog.send_message(error.args[0])

    def decrease_patient_status(self, patient_id: int):
        try:
            if not self.ent.approve_to_decrease_status(patient_id=patient_id):
                self.dialog.send_message(
                    'Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)'
                )
            else:
                self.ent.decrease_status(patient_id=patient_id)
                status_name = self.ent.get_status_name_by_patient_id(patient_id=patient_id)
                self.dialog.send_message(f'Новый статус пациента: {status_name}')
        except ExceptionNoPatientInHospital as error:
            self.dialog.send_message(error.args[0])

    def discharge_patient(self, patient_id: int):
        try:
            self.ent.discharge(patient_id=patient_id)
            self.dialog.send_message('Пациент выписан из больницы')
        except ExceptionNoPatientInHospital as error:
            self.dialog.send_message(error.args[0])

    @staticmethod
    def _convert_calculated_statistics_to_text(calculated_statistics_data, count_patients):
        result_calculated_statistics = f'В больнице на данный момент находится {count_patients} чел., из них: \n'
        for k, v in calculated_statistics_data.items():
            if v != 0:
                result_calculated_statistics += f'        в статусе "{k}": {v} чел. \n'
        return result_calculated_statistics

    def show_calculated_statistics(self):
        calculated_statistics_data = self.ent.get_calculated_statistics()
        count_patients = self.ent.get_count_of_patients()
        result_calculated_statistics = self._convert_calculated_statistics_to_text(calculated_statistics_data,
                                                                                   count_patients)
        self.dialog.send_message(result_calculated_statistics)
