import unittest
import io

from vehicle import *

class Test01_vehicle_instance_object(unittest.TestCase):
    def test_list_int(self):
        obj = Vehicle(engine_type="Hybrid",color="Blue")
        self.assertEqual(obj.engine_type, "Hybrid")
        self.assertEqual(obj.color, "Blue")
        self.assertEqual(obj.towing_capacity, 0)
        self.assertEqual(obj.wheel_type, "Tires")
        print()

class Test02_vehicle_class_variable(unittest.TestCase):
    def test_list_int(self):
        obj1 = Vehicle(engine_type="Hybrid",color="Blue")
        obj2 = Vehicle(engine_type="Gas",color="White")
        Vehicle.wheel_type = "Rims and Tires"
        obj1.color = "Black"
        self.assertEqual(obj1.color, "Black")
        self.assertEqual(obj2.color, "White")
        self.assertEqual(obj1.wheel_type, "Rims and Tires")
        self.assertEqual(obj2.wheel_type, "Rims and Tires")
        Vehicle.wheel_type = "Tires"
        print()

class Test03_car_instance_object(unittest.TestCase):
    def test_list_int(self):
        obj = Car(passengers=4, engine_type="Electric",color="Black")
        self.assertEqual(obj.engine_type, "Electric")
        self.assertEqual(obj.color, "Black")
        self.assertEqual(obj.towing_capacity, 0)
        self.assertEqual(obj.wheel_type, "Tires")
        self.assertEqual(obj.passengers, 4)
        print()

class Test04_car_class_variable(unittest.TestCase):
    def test_list_int(self):
        obj1 = Car(passengers=4, engine_type="Electric",color="Blue")
        obj2 = Car(passengers=5, engine_type="Gas",color="White")
        Car.vehicle_classification = "Passenger Car"
        obj1.passengers = 2
        self.assertEqual(obj1.passengers, 2)
        self.assertEqual(obj2.passengers, 5)
        self.assertEqual(obj1.vehicle_classification, "Passenger Car")
        self.assertEqual(obj2.vehicle_classification, "Passenger Car")
        Car.vehicle_classification = "Car"
        print()

class Test05_truck_instance_object(unittest.TestCase):
    def test_list_int(self):
        obj = Truck(passengers=4, engine_type="Electric",color="Black")
        self.assertEqual(obj.engine_type, "Electric")
        self.assertEqual(obj.color, "Black")
        self.assertEqual(obj.towing_capacity, 0)
        self.assertEqual(obj.wheel_type, "Tires")
        self.assertEqual(obj.passengers, 4)
        print()

class Test06_truck_class_variable(unittest.TestCase):
    def test_list_int(self):
        obj1 = Truck(passengers=4, engine_type="Electric",color="Blue")
        obj2 = Truck(passengers=5, engine_type="Gas",color="White")
        Truck.vehicle_classification = "Heavy Truck"
        obj1.passengers = 2
        self.assertEqual(obj1.passengers, 2)
        self.assertEqual(obj2.passengers, 5)
        self.assertEqual(obj1.vehicle_classification, "Heavy Truck")
        self.assertEqual(obj2.vehicle_classification, "Heavy Truck")
        Truck.vehicle_classification = "Truck"
        print()

class Test07_sedan(unittest.TestCase):
    def test_list_int(self):
        obj1 = Sedan(passengers=4, engine_type="Electric",color="Blue")
        obj2 = Sedan(passengers=5, engine_type="Gas",color="White")
        obj1.engine_type = "Hybrid"
        obj2.passengers = 6
        Car.vehicle_classification = "Passenger Car"
        Car.wheel_type = "Rims and Tires"
        Truck.vehicle_classification = "Heavy Truck"
        self.assertEqual(obj1.vehicle_classification, "Passenger Car")
        self.assertEqual(obj1.vehicle_type, "Sedan")
        self.assertEqual(obj1.wheel_type, "Rims and Tires")
        self.assertEqual(obj1.engine_type, "Hybrid")
        self.assertEqual(obj1.color, "Blue")
        self.assertEqual(obj1.doors, 4)
        self.assertEqual(obj1.passengers, 4)
        self.assertEqual(obj1.towing_capacity, 0)
        self.assertEqual(obj2.vehicle_classification, "Passenger Car")
        self.assertEqual(obj2.vehicle_type, "Sedan")
        self.assertEqual(obj2.wheel_type, "Rims and Tires")
        self.assertEqual(obj2.engine_type, "Gas")
        self.assertEqual(obj2.color, "White")
        self.assertEqual(obj2.doors, 4)
        self.assertEqual(obj2.passengers, 6)
        self.assertEqual(obj2.towing_capacity, 0)
        Car.vehicle_classification = "Car"
        Car.wheel_type = "Tires"
        Truck.vehicle_classification = "Truck"
        print()

class Test08_coupe(unittest.TestCase):
    def test_list_int(self):
        obj1 = Coupe(passengers=2, engine_type="Electric",color="Blue")
        obj2 = Coupe(passengers=3, engine_type="Gas",color="White")
        obj1.engine_type = "Hybrid"
        obj2.passengers = 1
        Car.vehicle_classification = "Passenger Car"
        Car.wheel_type = "Rims and Tires"
        Truck.vehicle_classification = "Heavy Truck"
        self.assertEqual(obj1.vehicle_classification, "Passenger Car")
        self.assertEqual(obj1.vehicle_type, "Coupe")
        self.assertEqual(obj1.wheel_type, "Rims and Tires")
        self.assertEqual(obj1.engine_type, "Hybrid")
        self.assertEqual(obj1.color, "Blue")
        self.assertEqual(obj1.doors, 2)
        self.assertEqual(obj1.passengers, 2)
        self.assertEqual(obj1.towing_capacity, 0)
        self.assertEqual(obj2.vehicle_classification, "Passenger Car")
        self.assertEqual(obj2.vehicle_type, "Coupe")
        self.assertEqual(obj2.wheel_type, "Rims and Tires")
        self.assertEqual(obj2.engine_type, "Gas")
        self.assertEqual(obj2.color, "White")
        self.assertEqual(obj2.doors, 2)
        self.assertEqual(obj2.passengers, 1)
        self.assertEqual(obj2.towing_capacity, 0)
        Car.vehicle_classification = "Car"
        Car.wheel_type = "Tires"
        Truck.vehicle_classification = "Truck"
        print()

class Test09_pickup(unittest.TestCase):
    def test_list_int(self):
        obj1 = Pickup(passengers=4, engine_type="Electric",color="Blue")
        obj2 = Pickup(passengers=5, engine_type="Gas",color="White")
        obj1.engine_type = "Hybrid"
        obj2.passengers = 6
        obj2.towing_capacity = 10000
        Truck.vehicle_classification = "Heavy Truck"
        Truck.wheel_type = "Rims and Tires"
        Car.vehicle_classification = "Passenger Car"
        Pickup.doors = 4
        self.assertEqual(obj1.vehicle_classification, "Heavy Truck")
        self.assertEqual(obj1.vehicle_type, "Pickup")
        self.assertEqual(obj1.wheel_type, "Rims and Tires")
        self.assertEqual(obj1.engine_type, "Hybrid")
        self.assertEqual(obj1.color, "Blue")
        self.assertEqual(obj1.doors, 4)
        self.assertEqual(obj1.passengers, 4)
        self.assertEqual(obj1.towing_capacity, 0)
        self.assertEqual(obj2.vehicle_classification, "Heavy Truck")
        self.assertEqual(obj2.vehicle_type, "Pickup")
        self.assertEqual(obj2.wheel_type, "Rims and Tires")
        self.assertEqual(obj2.engine_type, "Gas")
        self.assertEqual(obj2.color, "White")
        self.assertEqual(obj2.doors, 4)
        self.assertEqual(obj2.passengers, 6)
        self.assertEqual(obj2.towing_capacity, 10000)
        Truck.vehicle_classification = "Truck"
        Truck.wheel_type = "Tires"
        Car.vehicle_classification = "Car"
        Pickup.doors = 4
        print()

class Test10_suv(unittest.TestCase):
    def test_list_int(self):
        obj1 = SUV(passengers=5, engine_type="Electric",color="Blue")
        obj2 = SUV(passengers=5, engine_type="Gas",color="White")
        obj1.engine_type = "Hybrid"
        obj2.passengers = 7
        obj2.towing_capacity = 8000
        Truck.vehicle_classification = "Heavy Truck"
        Truck.wheel_type = "Rims and Tires"
        Car.vehicle_classification = "Passenger Car"
        SUV.doors = 6
        self.assertEqual(obj1.vehicle_classification, "Heavy Truck")
        self.assertEqual(obj1.vehicle_type, "SUV")
        self.assertEqual(obj1.wheel_type, "Rims and Tires")
        self.assertEqual(obj1.engine_type, "Hybrid")
        self.assertEqual(obj1.color, "Blue")
        self.assertEqual(obj1.doors, 6)
        self.assertEqual(obj1.passengers, 5)
        self.assertEqual(obj1.towing_capacity, 0)
        self.assertEqual(obj2.vehicle_classification, "Heavy Truck")
        self.assertEqual(obj2.vehicle_type, "SUV")
        self.assertEqual(obj2.wheel_type, "Rims and Tires")
        self.assertEqual(obj2.engine_type, "Gas")
        self.assertEqual(obj2.color, "White")
        self.assertEqual(obj2.doors, 6)
        self.assertEqual(obj2.passengers, 7)
        self.assertEqual(obj2.towing_capacity, 8000)
        Truck.vehicle_classification = "Truck"
        Truck.wheel_type = "Tires"
        Car.vehicle_classification = "Car"
        SUV.doors = 5
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
