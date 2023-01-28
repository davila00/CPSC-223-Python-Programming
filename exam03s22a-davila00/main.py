from vehicle import *

v1 = Sedan(passengers = 4, engine_type = "Electric", color = "Black")

v2 = Coupe(passengers = 2, engine_type = "Gas", color = "White")

v3 = Pickup(passengers = 2, engine_type = "Gas", color = "Red")
v3.towing_capacity = 10000

v4 = SUV(passengers = 7, engine_type = "Electric", color = "Gray")
v4.towing_capacity = 8000

mylist = [v1, v2, v3, v4]

for x in mylist:
    print("-------------------------------------------------------")
    print("vehicle_classification:", x.vehicle_classification)
    print("vehicle_type          :", x.vehicle_type)
    print("wheel_type            :", x.wheel_type)
    print("engine_type           :", x.engine_type)
    print("color                 :", x.color)
    print("doors                 :", x.doors)
    print("passengers            :", x.passengers)
    print("towing_capacity       :", x.towing_capacity)
