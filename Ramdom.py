import random

#By default the seed is set to local timestamp thus generating totally random nos every time the program is run
#if we set the seed manually then it would give the same order of nos every time the program is run

# random.seed(35)

#so either don't set the seed manually or else set seed=time_now
#random.random() takes no arguments
print(random.random())
print(random.random())
print(random.random())

numbers=[1,2,3,4,5,6,7,8,9,10]
names=['Yudhistir','Bheem','Arjun','Nakul','Sahdev']
print(random.choice(numbers))
print(random.choice(names))

print(random.choice('HelloMyNameIsSwarga'))

#want pick k unique values randomly from a set of n values
print(random.sample(names,4))