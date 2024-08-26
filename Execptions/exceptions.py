try:
    value=int(input('Please enter a number:'))
    print('The inverse of a number',value,'is',1/value)
except ValueError:
    print('Entered value is not a number!')
except ZeroDivisionError:
    print('Divison by Zero is not a valid operation!')

#SyntaxError by Python can only be caught by the except block if and only if it is raised in the try block ie it can only be caught if you intentionally raise/throw SyntaxError. If you mistakenly do some syntax error then Python would automatically raise a SyntaxError and it can't be caught by the except block.

#SystemExit is an exception which is only raised when we call the method sys.exit()

#Ways to raise exceptions on our own. One way is to use assertions. Assertions are certain assumptions in our program which are always true.

def calc_inverse(num):
    assert(num!=0),'Number is 0' # Assertion has a condition which we assume to be always true if the assertion is true then the control simply moves to the next line else the error is raise with error message.
    return 1/num

calc_inverse(4)