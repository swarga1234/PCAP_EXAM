class Vehicle:
    def __init__(self,speed):
        self.speed=speed

class LandVehicle(Vehicle): #LanVehicle inherits Vehicle. In Python the superclass is written in braces beside the subclass
    def __init__(self, speed,wheel_count):
        super().__init__(speed)
        self.wheel_count=wheel_count

class Car(LandVehicle):
    pass

print(issubclass(Car, LandVehicle)) # True, as Car is a subclass of LandVehicle
print(issubclass(LandVehicle,Vehicle)) #True as LandVehicle is a subclass of Vehicle
print(issubclass(Car,Car)) #True as a class is a subclass of itself

#Scenario1 : We have constructor in the super class Vehicle although we don't have a  constructor defined for the class Car. If we try create an object for Car then it will give error as the Car class has inherited the constructor from the super class Vehicle.

#my_car=Car() #Error Vehicle.__init__() missing 1 required positional argument: 'speed'
#This can be resolved by passing a speed value

my_car=Car(5,6)
print(my_car.__dict__)

#Scenario 2: We define a constructor in the LandVehicle. Now if we try to create the object of Car then it will inherit the constructor of class LandVehicle rather than the class Vehicle. 

# my_car=Car(5)
print(my_car.__dict__) #{'wheel_count': 5}

# Scenario 3: If we also want to access the properties of the class Vehicle then we can invoke the constructor of the class Vehicle in the subclass LandVehicle usig super
print(my_car.__dict__) #{'speed': 5, 'wheel_count': 6}