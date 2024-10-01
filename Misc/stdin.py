#take input from console and show it in the console
import sys

for line in sys.stdin:
    if line.rstrip()=='q': #on entering q the program will be terminated.
        break
    print(line)