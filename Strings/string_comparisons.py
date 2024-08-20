#Strings can by compared using all the relational operators which can be used to compare the numbers ie ==,!=,>,<.>=,<= etc

print('Python'=='Python') #True
print('Python'=='python') #False
print('Python'!='python') #True

#so we can see that str1==str2 is true only when str1 and str2 are identical i.e. all the letters of the str1 and str2 are same and even tha cases of the letters are also same. 

print('I love Python' < 'I love python') #This will give true. In python the two strings are compared letter by letter using the ascii values. So if see for the words Python and python the ascii code of P is 82 < ascii code of p (112 ? I guess). So the result will be true

print('Pythonist'>'Python') #This will give true. As both the words starts with Python so here the lengths will be checked. As length of Pythonist > Python , so this expression will give true.

print('Pythonist'>'PythonIs') #same logic as above

#The above logic only works if the longer string begins with the shorter string. Otherwise python checks for the ASCII values of the first differing indexes.

print('Pythonist'>'p') #In this case as the longer string 'Pythonist' does not  start with the shorter string 'p' as 'P' and 'p' are not equal. So in this case the ascii values of first differing characters or indexes are compared and ascii(P) < ascii(p) and thus in this case the answer is false.

print('20'>'8') #In this Python will give false. As Python is not comapring the nos 20 and 8 rather as they are in single quotes it is treating them as strings and thus here the comparision will be character by character. So, first '2' will be compared with '8' and as ascii of 8 > ascii of 2 so this returns false

#Comparing Strings with number. So a string can't be compared with a number. So only two operators "==" and "!=" can be used for comparison which will always return false no matter what. If we use other operators other than the above two we will TypeError

print(10=='Hello') #false
print(10!='Hello') #True as a number can't be equal to string. Can't compare apples with oranges.

print(10>'Hello') #TypeError