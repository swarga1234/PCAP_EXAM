#Create a class Rectangle and calculate the area

class Retangle:

    #Constructor. The constructor name is always __init__. By default the python constructor should have atleast one parameter. You can give any name but the convention is to name the parameter as self. self parameter is always pointing the object currently created within the constructor. You can provide default value to the self parameter but it will be simply ignored.
    def __init__(self,width, height):
        self.width=width
        self.height=height
    
    #self.varname means that the class will have the variable called varname. Unlike JAVA we have to mention the class variables inside the constructor only.

    #class method to calculate the area of the rectangle.
    def getArea(self):
        return self.width * self.height
    

rectangle=Retangle(10,12)
print(f"The area of rectange is: {rectangle.getArea()}")
