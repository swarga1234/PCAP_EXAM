#Lambda ar typically inline functions

#This is a classic function to add two nos
def sum(a,b):
    return a+b

print(sum(3,5)) #Gives sum of a+b

#lambda function to add 2 nos
lambda_sum=lambda a,b: a+b
print(lambda_sum(2,7))

#lambda functions can be passed as variables to other classic functions
do_square= lambda x: x*x

#lest write a classic function to square every element of a list
def square_every_element(elements, do_square):
    for num in elements:
        print(do_square(num))

elements=[1,2,2,3,4]
#Passing a lambda function as argument
square_every_element(elements, do_square)

#map() function works quite the same as yield in a classic function. It returns a iterator and accepts a lambda function and list as the argument. Based on the lamda func it returns the iteration of the modified list

double_element=lambda i: i*2
map_result=map(double_element,elements) #here map result is the iterator

print(next(map_result)) #Returns the first element of the modified list. Calling the next func will return the subsequent modified elements of the modified list

print(next(map_result))

#the better way is to use a for loop instead of next func
for num in map_result:
    print(num, end=",")
print("\n")
map_result=map(double_element,elements)
print(list(map_result)) #will print a list... convert the map result to list

#filter() function works quite similar to map() only that it is used to filter values from a sequence based on the lambda function
#filter only even values from the list
get_even=lambda i: i%2==0
# def even(elements, func):
#     for i in elements:
#         print(func(i))

# print(even(elements, get_even))
filter_res=list(filter(get_even,elements))
print(filter_res)

#Check for valid email addresses using filter
emails=[
    'swargasarkar.gmail.com',
    'swargasarkar@gmail.com',
    'xyx@gmail.com',
    '9887171'

]
valid_email=lambda i:'@' in i #valid email should contain @
print(list(filter(valid_email,emails)))

print(list(map(lambda x: x*2,(1,2,3,4,5,6,7,8,9))))
