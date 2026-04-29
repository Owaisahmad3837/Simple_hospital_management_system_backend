class Doctor:
  def __init__(self,doctor_id,name,specialization,phone):
    self.doctor_id=doctor_id
    self.name=name
    self.specialization=specialization
    self.phone=phone

  def to_dict(self):
    return self.__dict__
  