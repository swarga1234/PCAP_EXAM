first_num=5
second_num=5
print(first_num==second_num) # Compares the values of the 2 variables
print(first_num is second_num) #compares the references of 2 variables

first_num=5
second_num=2
second_num+=3
print(first_num==second_num) # Compares the values of the 2 variables
print(first_num is second_num) #compares the references of 2 variables

#For Integers if the values are equal then is operator returns true

first_str='Hello'
second_str='Hello'
print(first_str==second_str) #True Compares the values of 2 strings which is equal in this case.
print(first_str is second_str) #True. When a string var of same value exists previously then the new variable just points to the previous variable. Like in this case first_str is assigned the value Hello. When we create the second_str with same value then second_str is not assigned a new memory address rather it points the first_str. So first_str is second_str is true. Similar concept to String Pool in JAVA.

first_str='Hello'
second_str='Hell'+'o'
print(first_str==second_str) #True Compares the values of 2 strings which is equal in this case.
print(first_str is second_str) #True. As 'Hell'+'o' is "Hello" and concatenation is done before assigning the value to second_str and so no new string is created and second_str points to the same memory as of first_str

first_str='Hello'
second_str='Hell'
second_str+='o'
print(first_str==second_str) #True Compares the values of 2 strings which is equal in this case.
print(first_str is second_str) #In this case value of second_str is 'Hell' and the +'o' which when concatenated gives 'Hello' which is equal to first_str but as Strings are immutable so when we try to modify the second_str its creates a new string which is allocated a memory different from first_str. So The answer is False

first_str='Hello'
second_str='Hell'
second_str+='o'
third_str=second_str
print(first_str==second_str) #True Compares the values of 2 strings which is equal in this case.
print(first_str is third_str)#False
