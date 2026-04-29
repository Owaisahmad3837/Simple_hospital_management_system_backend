class Patient:
  def __init__(self,patient_id,name,age,gender,phone):
    self.patient_id=patient_id
    self.name=name
    self.age=age
    self.gender=gender
    self.phone=phone

  def to_dict(self):
    return self.__dict__