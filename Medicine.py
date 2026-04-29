class Medicine:
  def __init__(self,medicine_id,name,price):
    self.medicine_id=medicine_id
    self.name=name
    self.price=price
  
  def to_dict(self):
    return self.__dict__
  
