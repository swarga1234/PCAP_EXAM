# Class variable is stored in the class and has only one copy. It can be accessed outside the class even with creating the object of the class. In easy words it is basically static variable.

class Dog:

    counter=0 # this is class variable. It is created outside the constructor and defined with no reference to self.
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Dog.counter+=1
    #__str__ method is the python equivalent of the java method toString(). It does exactly the same work
    def __str__(self):
        return "Dog name: "+self.name+" Dog age: "+str(self.age)+" Dog Count: "+str(Dog.counter)

my_pet_1=Dog('Bullock',5)
my_pet_2=Dog('Rocky',4)
my_pet_3=Dog('Tommy',4)

print(my_pet_1)

print(my_pet_1.counter)
print(my_pet_2.counter)
print(my_pet_3.counter)

#All the 3 above statements will have same output as the class var/static var counter has only one copy and thus no new copies are created each for the objects my_pet_1,my_pet_2,my_pet_3.

print(my_pet_3.__dict__) #It will only show the instance variables and not the class variable 'counter'. {'name': 'Tommy', 'age': 4}

print(Dog.__dict__) # It will show only the class variables of the class Dog

class Cat:

    __counter=0 # this is class variable. It is created outside the constructor and defined with no reference to self. This variable is made private using __ as prefix.
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Cat.counter+=1

#The private class variable will also be name mangled.
#print(Cat.__counter)#AttributeError
print(Cat._Cat__counter) #the mangled varible for the __counter var is _Cat__counter (_classname__varname)
print(Cat.__dict__)

#hasattr(class/Object name, property name) is ued to check if attribute is available for a object or in the class

if hasattr(my_pet_1,"name"):
    print("My pet is called",my_pet_1.name)

if hasattr(Cat, "_Cat__counter"):
    print("My cat has a counter")

#__name__ attribute is used to print the name of the class. It can only be called using the class and not the object
print(Dog.__name__) #Dog

#type is used to return the type of the object. IN combination with the __name__ attribute it will return the name of the class of the object 
print(type(my_pet_1).__name__)

#__module__ propety returns name of the module of which the class is part of. If the class is in the same file from where the __module__ is called then it will return __main__
print(Cat.__module__)