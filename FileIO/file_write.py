#writing in to file
try:
    stream=open('newfile.txt','w') # w stands for write mode. In write mode either a new file will be created if the file doesn't exists or if exists then then the older file will deleted and a fesh file of same name will be created!
    stream.write("This is the first message!\n")
    stream.write("This is the second message!")
    stream.close()
except Exception as e:
    print("An error occured!",e)