empty_list=[] #empty lists
cities=['Mumbai', 'Delhi', 'Kolkata','Pune','Hyderabad']
print(cities[1:]) #elements from index 1 to end
print(cities[-1]) # prints the last element
print(cities[-2]) # prints the 2nd last element
print(cities[-1:]) # prints the last element to the last element ie only the last element in form of list
print(cities[:-1]) # Prints the whole list excluding the last element
print(cities[1:3]) #prints the elements from ith index to j-1 th index
print(cities[1:9]) #Will not give an error when you enter an index 9 which is out of the range of the list while slicing. It will just print the list from ith index to the end index
print(cities[1:-1]) #-1 represents the last index. so from ith index to 2nd last index
print(cities[:]) #prints the whole list, same as print(cities)
print(cities)
print(cities[90:100]) # with both the start and end indices are non existent in this case so it wil just print an empty list.

#del a value from list
del cities[3] #Deletes the value at index 3
print(cities)

#delete the whole list
del cities
#print(cities) #Error as the list cities has been deleted

#reinitialising the list
cities=['Mumbai', 'Delhi', 'Kolkata','Pune','Hyderabad']

#Adding a new value to the list
cities.append('Amdavad') # Append the new value at the end of the list

print (cities)

#inserting an element at specific position in the list
cities.insert(3,'Bangalore') #insert the value at index 3 in the list

print(cities)

#Swapping elements
cities[2],cities[3]=cities[3],cities[2]
print(cities)

#Sorting lists. The list containing the strings will be sorted alphabetically and the list containing numerics will by sorted from ascending to descending by default.
cities.sort()
print(cities) # The original list itself is being altered

list_original=[1,2,3]
list_new=list_original
list_original[2]=-3
list_new[1]=-5
print("Original:",list_original)
print("New:",list_new)

#In the above case when we try to modify the list_original it is refekected in the list_new and vice versa. This happens because list_new becomes a referenece to the list_original and thus both of them just point to the same memory address and so modifying one will be reflected in other. However assigning list_original to the list_new may not be reasonable for our purpose like if we want to modify the list_original and later we want to compare the current values of the list_original with the previous values of the list_original, then using this technique will change both the lists and we may never have the original values. Thus in this case we will have to slice the list_original when we assign its value to the list_new. This will ensure that modifying one will not be reflected on both the lists.

list_original=[1,2,3]
list_new=list_original[:]
list_original[2]=-3
list_new[1]=-5
print("Original:",list_original)
print("New:",list_new)

#List Comprehensions
numbers=[i for i in range(1,101)] #will create a list containing every number from 1 to 100.
print(numbers)

numbers=[i for i in range(1,101) if i%3!=0] # Will create a list with numbers from 1 to 100 which are not a multiple of 3
print(numbers)

# Multi Dimensional lists
table=[['A1','A2','A3'],['B1','B2','B3']]
print(table[0])
print(table[0][0])

#Traverse a multi dimensional list
for row in table:
    for cell in row:
        print(cell, end=' ')
    print()

#Creating  a list using list comphresion. Create a 2D list containing nums 1 to 5 in each row and there are 4 rows in total

table=[[i for i in range(1,6)] for j in range(4)]
print(table)

nums=[1,2]*10
print(nums) #Creates a list containing 10 pairs of 1,2
