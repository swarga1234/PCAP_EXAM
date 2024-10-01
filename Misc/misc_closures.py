#A Closure is a function defined inside another function but remembers the values of the outer function
def greet(text):
    def print_greet():
        print(text)
    return print_greet

say_hello=greet("Hello")
say_hello()

#the inner function "print_greet" is called closure
#So if we see technically when we are calling the function say_hello() the scope of the variable "hello" which is passed to greet() function has already ended thus these variables which are still available after the function call althought the scope has been destroyed are called free variable.

#Lets take a complex argument
def multiply_closure(x):
    def multiply(y):
        return x*y
    return multiply

multiply_5=multiply_closure(5)
multiply_12=multiply_closure(12)

print(multiply_5(10))
print(multiply_5(20))
print(multiply_12(10))
print(multiply_12(20))
