class Vehicle():
    """docstring for Vehicle."""

    wheel_type = "Tires"

    def __init__(self, *, color, engine_type):
        self.color = color
        self.engine_type = engine_type
        self.towing_capacity = 0


class Car(Vehicle):
    """docstring for Car."""

    vehicle_classification = "Car"

    def __init__(self, *, color, engine_type, passengers):
        Vehicle.__init__(self, color = color, engine_type = engine_type)
        self.passengers = passengers


class Truck(Vehicle):
    """docstring for Truck."""

    vehicle_classification = "Truck"

    def __init__(self, *, color, engine_type, passengers):
        Vehicle.__init__(self, color = color, engine_type = engine_type)
        self.passengers = passengers


class Sedan(Car):
    """docstring for Sedan."""

    vehicle_type = "Sedan"

    doors = 4


class Coupe(Car):
    """docstring for Coupe."""

    vehicle_type = "Coupe"

    doors = 2


class Pickup(Truck):
    """docstring for Pickup."""

    vehicle_type = "Pickup"

    doors = 2

class SUV(Truck):
    """docstring for SUV."""

    vehicle_type = "SUV"

    doors = 5
