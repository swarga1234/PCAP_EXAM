#The most basic way to read a file
try:
    stream =open('animals.txt')
    #code
    print(stream.read())#reads till eof 
    #alternatively the read() also takes bytes as input and thus u can speify how many bytes you want to read. If the number of bytes are more than the total no of bytes in the file then it will juts print the whole file no exception will happen
    print(stream.read(10)) #this will print nothing as already the stream is at the eof so it will just print a blank line
    stream.close()
except Exception as e:
    print(e)

#Reading a file character by character
try:
    stream=open('animals.txt')
    character=stream.read(1) #reads 1 byte= 1 character at a time
    while character!='':
        print(character, end='')
        character=stream.read(1)
    stream.close()
except Exception:
    print(e)

print("\n")
#Reading a file line by line
try:
    stream=open('animals.txt')
    line=stream.readline() #reads 1 line at a time
    while line!='':
        print(line, end='')
        line=stream.readline()
    stream.close()
except Exception:
    print(e)

#Reading a file line by line using readlines. readlines return a list of lines.
try:
    stream=open('animals.txt')
    lines=stream.readlines() 
    while line in lines:
        print(line)
    stream.close()
except Exception:
    print(e)

#Better way to use readlines. Don't read the whole file at once
print('Better way to use readlines')
try:
    stream=open('animals.txt')
    line=stream.readlines(2) #reads a whole line at once
    while len(lines)!=0:
        for line in lines:
            print(line)
        lines=stream.readlines(2)
    stream.close() #After stream.close() only calling stream.close() will not raise any error.
except Exception:
    print(e)

#using stream as it is a iterator
print("\nUsing Stream as iterator")
try:
    stream=open('animals.txt')
    for line in stream:
        print(line, end='')
except Exception:
    print(e)