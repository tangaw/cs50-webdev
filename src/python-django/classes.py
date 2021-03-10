class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passenger(self, name):
    if not self.open_seats():
      return False
    else:
      self.passengers.append(name)
      return True

  def open_seats(self):
    return self.capacity - len(self.passengers)


names = ["Aaron", "Sean", "Tom", "Evan"]

f = Flight(3)
for name in names:
  if f.add_passenger(name):
    print(f"{name} was successfully added")
  else:
    print(f"There is no room for {name}")
    