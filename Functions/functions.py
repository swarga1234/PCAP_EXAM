def greet():
    print("Hello Swarga!")


input_nums=[1.0, 2.3, 4.5, 6.7]

def getAvg(input_nums):
    sum=0.0
    for num in input_nums:
        sum+=num
    avg=sum/len(input_nums)
    print(avg)

print_var=print("Hello Swarga!!")
print(print_var) #the print() function returns the value None. The functions which don't return anything returns None
#None is similar to null in java. 

x=None

#Various ways to check for None
if x:
    print('None is True!')
elif x is False:
    print('None is False')
else:
    print('None is only None!')

if x is None:
    print('x is None')

if x==None:
    print('x is also None')


#Generators are used to generate a sequence of values. The generator function remembers the last last returned valued and use it to return the next.

def generate_nums():
    for num in range(1,4):
        yield num #In generator function yield is used in place of return

#we can store the value of the generator function in a variable and the next function can be used to generate the next number in the sequence

generated_nos=generate_nums()
print(next(generated_nos)) #1
print(next(generated_nos)) #2 
print(next(generated_nos)) #3
#print(next(generated_nos)) #StopIteration as the loop in the func generate_nums() runs from 1 to 3

#it can be also used in for loop to get all the nos of the sequence
for i in generate_nums():
    print (i)

#It can also be used to populate the lists
num_list=list(generate_nums())
print(num_list)
# greet()

# getAvg(input_nums)