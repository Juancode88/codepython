"""
Write a program to print a sequence
of the alphabet letters in a pyramid,
the sequence should be orderly
without repeat either letter.the
user would enter the pyramid row
amount
"""
n = int(input("How many rows are?:"))
def seq_alphabet(n):
    num = 65
    k = n - 1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0,i+1):
            character = chr(num)
            print(character,end=" ")
            num = num + 1
        print("\r")
seq_alphabet(n)