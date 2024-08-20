# The Platform module can tell you about the Python version, operating system and the Hardware you are using.
import platform

print(platform.platform()) #Gives the details of the OS
#the platform.platform(aliased=bool, terse=bool) has 2 parameters which are by default set to false.
#if aliased is set to true then it will show some aliased name of the OS if available.
#terse if set to true it will show a a shorter name/ version of the OS
#when both are set true it will show aliased and shorter name of the OS
print(platform.platform(aliased=True,terse=True))

# This returns the Generic name of the processor of the machine on which the program is running
print(platform.machine())

#This returns the real/full name of the processor on which program is running
print(platform.processor())

#This function prints the generic name of the system on which program is running like windows/mac
#For MAC it is hsowing Darwin
print(platform.system())

#This function prints the implementation of Python that is being used. CPython is the most widely implemented version of Python
print(platform.python_implementation())

#this prints a tuple in which the elements are in the order (major_version, minor_version, patching_version)

print(platform.python_version_tuple())

#This prints the system's release version as a single string
print(platform.version()) #Don't confuse this with platform.python_version_tuple()
print(platform.python_version()) # prints the python version