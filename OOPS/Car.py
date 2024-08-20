# Class to emulate the functionalities of a car

class Car:

    #create constructor
    #initial_speed=0 is a default argument hence if value of initial_speed is passed while creating teh object the it will be by default set to 0
    def __init__(self, model, color, initial_speed=0):
        self.model=model
        self.color=color
        if initial_speed < 0: #initial_speed can't be -ve 
            self.__speed=0
        else:
            self.__speed=initial_speed # Adding __ as prefix to the name of the property makes it private and it can't be modified from outside.
    
    # A method to increase the speed of the car
    def speed_up(self):
        self.__speed+=5
    
    # A method to decrease the speed of the car
    def slow_down(self):
        #speed of car can't be less than 0. 
        if self.__speed >=5: 
            self.__speed-=5
        else:
            print('As slowing down will make the speed -ve so setting it to 0')
            self.__speed=0

    # Show the speed
    def show_speed(self):
        print("The current speed of teh car is: ",self.__speed)
    

my_car=Car('MS-Alto','red') #passing the intial speed as 5km/hr. If not passed it will automatically set to 0
my_car.__speed=50 #So even if we set the speed to 50, because speed is a private variable so the value of speed will still remain 5 which was set using the constructor.
my_car.speed_up()
my_car.show_speed()
my_car.slow_down()
my_car.slow_down()
my_car.show_speed()

