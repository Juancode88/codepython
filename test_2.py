"""
Python program that Counting the Number of occurrences of a 
Character in a String and Reversing a String using an 
Extended Slicing Technique "sequence[start:stop:step]"
"""
string = input("What is the string?:").lower()
character = input("What is the character:").lower()
count_c = 0
for letter in string:
    if letter == character:
        count_c +=1
print(f"The amount occurrences are {count_c}")
print(f"The reverse string:{string[::-1]}")