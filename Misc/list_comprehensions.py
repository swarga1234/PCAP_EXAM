#List Comprehensions

#Storing nos from 1 to 100 in a list using for loop
new_list=[]
for i in range(1,101):
    new_list.append(i)

print(new_list)

#the Above step can be done in a single line using lits comprehensions
new_list=[i for i in range (1,101)] #Stores  1 to 100 in a list
print(new_list)

#Only want to store the even nos
new_list=[i for i in range(1,101) if i%2==0]
print(new_list)

#Only want to store 0's and 1's alternately
new_list=[0 if i%2==0 else 1 for i in range(1,101)]
print(new_list)

#Creating a 2D list with 1 to 5 nums in each row and total of 5 rows
list_2D=[[i for i in range(1,6)] for j in range(4)]
print(list_2D)

a,b=10,20
print((lambda: b, lambda: a)[a<b]())