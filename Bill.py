class Bill:
  def __init__(self,bill_id,patient_id,appointment_id,total_amount):
    self.bill_id=bill_id
    self.patient_id=patient_id
    self.appointment_id=appointment_id
    self.total_amount=total_amount

  def to_dict(self):
    return self.__dict__
  