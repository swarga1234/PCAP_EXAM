# Class to demonstrate the instance variables in Python
class Dog:

    def __init__(self, name, age):

        #so we are initialising 2 properties of the class Dog in the constructor
        self.name=name
        self.age=age

my_pet = Dog('Tommy',2)
print(my_pet.__dict__) #__dict__ prints the availables properties of a class and its values

my_pet.color= 'Brown' #So are creating a new property called color eventhough it was not defined in the original class or its contructor
print(my_pet.__dict__) #__dict__ prints the availables properties of a class and its values

del my_pet.name #We are deleting the property name usinf del keyword, although it was defined int the constructor of teh class Dog
print(my_pet.__dict__) #__dict__ prints the availables properties of a class and its values

#Lets create a class Cat for more examples
class Cat:

    def __init__(self, name, age):

        #so we are initialising 2 properties of the class Dog in the constructor
        self.__name=name #lets make the name variable private 
        self.age=age
    
my_cat= Cat('Tom',3)
print(my_cat.__dict__)
# As the name variable is private so output of the above code is {'_Cat__name': 'Tom', 'age': 3}. So we can see that the name of the private variable __name which was the original property of the class Cat has been changed to '_Cat__name'. So as the property __name property does not exist in the class Cat now so we can access or modify the __name from outside the class. Thus limiting the access to the property and making it private. This process is called Name mangling.

#print(my_cat.__name) # This will give AttributeError

#However in python the properties can't truely be private. In this case eventhough we can't access the property __name as it has been replaced by the name mangled property '_Cat__name'. But we acess the mangled property itself '_Cat__name' from outside the class thus making it again vulnerable. So, in python the variables can't truely be private. __propname is only a convention for the user to make him know that this variable is private and its value should not me modified outside the class.

#creating a new property color
my_cat.__color="White" # making the property color private using ___ as private. But as we are doing this outside the class so the name mangling  doesn't work thus __ doesnot really have any effect

print(my_cat.__dict__) #{'_Cat__name': 'Tom', 'age': 3, '__color': 'White'}. No name mangling for the property __color.

print(my_cat.__color) # white. No error as name mangling does not work for properties defined outiside the class.