class Appointment:
  def __init__(self,appointment_id,patient_id,doctor_id,date,disease):
    self.appointment_id=appointment_id
    self.patient_id=patient_id
    self.doctor_id=doctor_id
    self.date=date
    self.disease=disease

  def to_dict(self):
    return self.__dict__
  
  