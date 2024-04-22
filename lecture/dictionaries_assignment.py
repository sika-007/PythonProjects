my_vehicle = {
  "model": "Ford",
  "make": "Explorer",
  "year": 2018,
  "mileage": 4000
}

for x, y in my_vehicle.items(): 
  print(x + ": " + str(y))
  
vehicle_2 = my_vehicle.copy()

vehicle_2["number_of_tires"] = 4

vehicle_2.pop("mileage")

print(vehicle_2.keys())