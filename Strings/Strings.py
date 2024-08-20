print(len('Hi There!')) #Gives the length of the string
print('Hi There!'[3]) #Gives the i'th index of the String
print('Hi Theres!'[1:]) #Returns the string from ith character to the end
print('Hi Theres!'[:5]) #Returns the string until ith (ith char is excluded) character from the start
print('Hi Theres!'[3:6]) #Returns the string from ith character to jth (excluded) character
print('I\'m Swarga') #Return I'm Swarga. \' represents '
print(ord('a')) #Returns the ASCII value of a character
print(chr(65)) #Returns the char for the gives number. In this 'A' for the input 65.

#For representing multiline strings you need to enclose the string in '''
multi_line_string='''Line 1
Line 2'''

print(len(multi_line_string)) #This will return 13 in this case. There are 12 characters including alphabets, numerics, special characters and spaces. The 13 th one is the escape character \n which represents newline and in this case it is invisible

#iterating over a string
for char in 'hello from the world of python':
    print(char,end='-') #h-e-l-l-o- -f-r-o-m- -t-h-e- -w-o-r-l-d- -o-f- -p-y-t-h-o-n- (ans)

#Strings in Python are immutable like java
print('\n')
print(min('Ilovetravelling')) #Prints the character with least ASCII value. In this case I has the least value

print(min('I love travelling')) #In this case space has the minimum ascii value ie 32
print(max('I love travelling')) #Prints the character with the highest ASCII value 

#Printing the index of the first occurence of a letter/substring
print('IloveTravellingAroungTheWorld'.index('av'))

#Doing the same using find
print('IloveTravellingAroungTheWorld'.find('av'))

#Both find and index gives the same result. The only key differences are that index raises an error if the substring is not found while find returns -1. Moreover index can be used for other typesof sequences like lists apart from Strings. While find can only be used with strings.

print('IloveTravellingAroungTheWorld'.find('ab')) #As the substring ab in not present hence it will return -1

print('IloveTravellingAroungTheWorld'.find('av',8)) # In this the first args represents the substring to find and the second args is the index (inclusive) from which the find function will search for the substring

print('IloveTravellingAroungTheWorld'.find('ng',8,15)) #In this case second args is the first index(inclusive) from which find will search for the substring and the third args is the end index(exclusive) till which substring will be searched.

#rfind is a similar function to find except that is will start finding from the right of the string as opposed to left of the string which is the general convention
print('IloveTravellingAroungTheWorld'.rfind('ng'))
print('IloveTravellingAroungTheWorld'.rfind('ove',8)) #The second args represents the index of the string till which rfind will try to find the substring. If not present till that index it will return -1;

print('IloveTravellingAroungTheWorld'.rfind('ove',0,8)) #In this case second args is the first index(inclusive) from which find will search for the substring and the third args is the end index(exclusive) till which substring will be searched. Similar to the find function.

print('Swarga'.isalnum()) #returns true/false if the string only contains alphanumeric characters.
print('Swarga30'.isalnum()) #will return true as string only contains alphanumeric characters
print('Swarga_30'.isalnum())#will return false as string contains '_' which is not an alphanumeric character

print('Swarga'.isalpha()) #returns true if the string only contains alphabets.
print('123'.isdigit()) #returns true if the string only contains digits.

#join function: can join a list/sequences of strings using a separator
separator=' '
print(separator.join(['This is','a spectacular place','to be']))

#split function can split a string in to a number of substrings based on separtor, whitspace of new line \n character

print('How many\nstrings will\nyou see?'.split())

print('How many\nstrings will\nyou see?'.split('\n')) # only split based on new line \n characters

#Sorting a list of strings using sorted function

names=['Yudhisthir', 'Bheem', 'Arjuna', 'Nakul', 'Sahadev']

names_sorted=sorted(names) #sorted function sorts the list but does not modifies the actual list. 

print(names_sorted) #a new sorted list is return
print(names) #old unsorted list as the original list is not modified by the sorted function.

#sorting a list using sort function
names.sort() #Sorts the orginal list and does returns a sorted copy of the list
print(names) #the actual list has been sorted

print(len('\'\\')-len('\n')) #len('\'\\') is 2 (escape characters are also counted), len('\n') is 1

#print(float('1,3')) #valueError: could not convert string to float
print(float('1.3')) # ans 1.3

#Notes :
#Code point is a number that represents a character

print("Hello Swarga")
print("Learning Python!")
#So the above 2 lines will be printed on 2 different lines as by default the \n character is added to the end of each string. Lets Say we want to change this \n to any other value like '.'. We can do this using the keyword argument.

print("Hello Swarga", end='.')
print("Learning Python!")
#The output of the above 2 print statements will be "Hello Swarga.Learning Python!". The argument end is optional as it has a default value '\n' set. So, if you don't pass the value of end then by default it should use \n.

first_name='Swarga'
print("Hi!",first_name,"Welcome to Python course!!")

#The output of the above statement is Hi! Swarga Welcome to Python course!!. So if we look carefully we pass 3 strings as arguments separated by ',' to the print function. In the output these 3 strings are printed in the same order separated by spaces. So the default separator for the print function is Space. So Incase you don't provide a "sep" argument all the input parameters of the print function will be printed with space as the default separator. We can also pass our own separtor to the sep argument to change the default separator to our choice.

print("Hi!",first_name,"Welcome to Python course!!",sep='-')#Here we are passing '-' as our separator
#So in the above case our 3 arguments "Hi!" "Swarga" and "Welcome to Python course!!" will be separated by '-'. So the output will be "Hi!-Swarga-Welcome to Python course!!"

# In Strings indexing can't be used to change a character of a string in python

#first_name[2]='k'
#print(first_name) #TypeError: 'str' object does not support item assignment
