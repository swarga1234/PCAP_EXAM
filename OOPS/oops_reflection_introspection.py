#In many object oriented languages there are two types of special operations : Introspection and Reflection.
#Introspection: Introspection is the ability of the program to check the type of an object or its properties at runtime.
#Reflection: Reflection is the ability of a program to change the properties or methods of an object at runtime

#Lets now write an function which will take an object as argument and will set all the properties of the object which are string to blank or empty string

from oop_clazz_variables import Dog
def empty_strings(user_object):

    for prop_name in user_object.__dict__.keys():
        prop_value=getattr(user_object,prop_name)
        if isinstance(prop_value,str):
            setattr(user_object,prop_name,'')

my_dog=Dog('Tommy',5)
print(my_dog)

empty_strings(my_dog)
print(my_dog)

