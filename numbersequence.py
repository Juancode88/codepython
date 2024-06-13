"""
Write a program to print a number sequence,
each line has the same amount the numbers
according to the number row and the 
sequence not stop between the lines.also
the user should enter the rows amount.
""" 
n = int(input("How many are rows?:"))
def line(n):
    line = 1
    for i in range(0,n):
        for p in range(0,i+1):
            print(line,end=" ")
            line = line + 1
        print("\r")
line(n)       
