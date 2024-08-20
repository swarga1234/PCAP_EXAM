#dicts stores the values in key and value pairs and the values in an dictionary can be accessed by the keys which are unique in nature

#Lets create a english to bengali dictionary
english_to_bengali={
    'dog':'kukur',
    'cat':'biral',
    'elephant':'hati',
    'stupid':'ujbuk',
    'utter idiot':'udgandu'
}

print(english_to_bengali)
#translation for stupid in bengali
print(english_to_bengali['stupid'])

# The keys of a dict should be of immutable datatypes ie the key can be strings, integer or even tuples but can't be of list dataype.

#create an empty dictionary
grades={}

#add values to dictionary using keys
grades['Swarga']='B+'
grades['Soumya']='A-'

print(grades) #{'Swarga': 'B+', 'Soumya': 'A-'}

# length of the dictionary
print(len(grades))

#To check if a key is present in a dictionary
if 'Soumya' in grades:
    print('Soumya\'s marks:',grades['Soumya'] )

#Del a key value pair
del grades['Swarga']

print(grades)

grades['Swarga']='B+'
print(grades)

#Update a value in dictionary
grades['Swarga']='B'
print(grades) #Updated dict {'Soumya': 'A-', 'Swarga': 'B'}

#Using update function
grades.update({'Soumya':'A'})
print(grades)#Updated dict {'Soumya': 'A', 'Swarga': 'B'}

grades.update({'Toshali':'A'}) # Also adds a new key value pair to dict
print(grades)

#Iterating through dict

#Get the keys in the dict
for student_name in grades:
    print(student_name)

#Another way to get the key
for student_name in grades.keys():
    print(student_name)

#Get values in the dict
for grade in grades.values():
    print(grade)

#Get both the key and value pair in dict
for student_name,grade in grades.items():
    print(student_name,'got',grade)