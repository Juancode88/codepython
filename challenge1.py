"""
Write a program to print a arrow 
with asterisks sequence and the 
user would enter the arrow size 
in lines 
"""
n = int(input("What is the size?:"))
def arrow(n):
    k = 0
    for i in range(n , 0 , -1):
        for j in range(0,k):
            print(end=" ")
        k = k + 1
        for j in range(0,i):
            print("*",end=" ")
        print("\r")
arrow(n)
