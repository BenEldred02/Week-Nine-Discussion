import time

print("Welcome to your new personal garage!")
print("")

time.sleep(1)

class Vehicle:

  def setMake(self, make):
    self.str_make = make

  def setModel(self, model):
    self.str_model = model

  def getMake(self):
    return self.str_make

  def getModel(self):
    return self.str_model

class Car(Vehicle):

  def setDoors(self, doors):
    self.str_door = doors

  def getDoors(self):
    return self.str_door

class Truck(Vehicle):

  def setBedLength(self, bedLength):
    self.str_bedlength = bedLength

  def getBedLength(self):
    return self.str_bedlength

selection = 0
while int(selection) < int(3):
  selection = input("Please enter '1' for a car, '2' for a truck or '3' to quit this application: ")
  print("")
  if (selection == '1'):
    new_car = Car()
    strMake = input("Please enter the cars make: ")
    new_car.setMake(strMake)
    strModel = input("Please enter the cars model: ")
    new_car.setModel(strModel)
    strDoors = input("Please enter the number of doors: ")
    new_car.setDoors(strDoors)
    print("")
    print(f"The cars make is: {new_car.getMake()}")
    print(f"The cars model is: {new_car.getModel()}")
    print(f"The number of car doors is: {new_car.getDoors()}")
    print("This car has been added to your garage.")
    print("")
  elif (selection == '2'):
    new_truck = Truck()
    strMake = input("Please enter the trucks make: ")
    new_truck.setMake(strMake)
    strModel = input("Please enter the trucks model: ")
    new_truck.setModel(strModel)
    strLength = input("Please enter the bed length: ")
    new_truck.setBedLength(strLength)
    print("")
    print(f"The trucks make is: {new_truck.getMake()}")
    print(f"The trucks model is: {new_truck.getModel()}")
    print(f"The trucks bed length is: {new_truck.getBedLength()}")
    print("This truck has been added to your garage.")
    print("")
  else:
    print("")
    print("Thank you for using this program.")
    print("")