#MRO: Method Resolution Order:
#1.In this Python tries to find the method in the object itself which is calling the method. If available it will invoke the method.
#2. If the object does not have the method Python tries to look it up in the superclasses of the object. If only one copy is avialable the it invokes the method. However in case of multiple inheritance when a class has 2 or more super class then Python scans from left to right in the order of which the superclasses has been extended. The leftmost class to contain the method is invoked.
#3. If the method is not present at all then error is raised

class Vehicle:

    def drive(self):
        print('I am driving!')
    
    def introduce(self):
        print('I am Vehicle ')

class Flyable:
    def fly(self):
        print('I am Flying!')
    
    def introduce(self):
        print('I am Flyable ')


class Ariplane(Flyable,Vehicle):
    pass

my_plane=Ariplane()

my_plane.drive() #drive is only present in Vehicle class hence no conflict
my_plane.fly() #fly is only present in Flyable class hence no conflict
my_plane.introduce()#Here is the conflict as the method introduce is present in both the superclasses. Now as both the super classes are on the same level this poses a different kind of challenge on which version of the method to invoke. In this case MRO is followed and if the Vehicle class is leftmost extended method with the method then the output will be : I am Vehicle. Else if the leftmost extended class is Flyable then the output should be I am Flyable.

print(Vehicle.__bases__) # Return the base classes of Vehical as tuple. In this case Vehicle has only one base class and that is the default base class of all classes ie Object
print(Flyable.__bases__) # Same as Above.
print(Ariplane.__bases__) # As Airplane extends both the classes so (<class '__main__.Flyable'>, <class '__main__.Vehicle'>). Note : Object class is not the base class if the class already has base class other than Object

