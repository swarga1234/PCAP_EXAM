empty_tuple=() #Creates an empty tuple
one_el_tuple_a=(1,) #The comma is mandatory at the end if the tuple only has 1 element
one_el_tuple_b=1, #The comma is mandatory at the end if the tuple only has 1 element or else the interpreter can differentiate between normal assignment and tuple.
three_el_tuple=1,2,3 # the last comma if there are more than on element is not mandatory
print(three_el_tuple)

#Unlike lists tuples are immutable. So the tuple varible can be assigned a different tuple but the existing tuple elements can't be changed and deleted

# del three_el_tuple[1] #TypeError: 'tuple' object doesn't support item deletion
# print(three_el_tuple)

#Operations in tuple
user_data =('Swarga','Indian',1998)
print(len(user_data)) #prints the number of elements in the tuple

#checking if an element is present in the tuple
if 'Indian' in user_data:
    print("This person is from India!")
else:
    print("This person is Foreigner!")

#Addition in tuples. Similar to the concatenation of 2 strings
user_data=('Swarga','Indian',1998)+('Durgapur','WB')
print(user_data)
#As tuples are immutable so the addition of 2 tuples does not alter any of the existing tuples but creates a new tuple which is again assigned to user_data

#same with multiplication
num=(1,2)*10
print(num)

#tuple inside list
capital_1=("New Delhi","India",15)
capital_2=("Canberra","Australia",0.4)
capital_3=("London","UK",8)

#an example of tuples within a list
capitals=[capital_1,capital_2,capital_3]

#accessing each element of tuple with the list.
for capital in capitals:
    print("Capital_City:",capital[0],"Country:",capital[1],"Population:",capital[2])

#So here even though we can add more tuples to the list but we can't really change the elements of the individual tuples.

#List in tuples.
user_swarga=('Swarga','Indian',1998,[45,49,54,60,55]) # weights of the user every year

#In this case even though we can't modify the elements of the tuple like name of the user or the nationality of the user or we can't add another list in the tuple but we modify the mutable element of the tuple ie the list. We can add new elemnets to the weight_list/modify weights in the weight_list which is part of the tuple.

user_swarga[3].append(54)
print(user_swarga)