"""
Python program that Counting vowels & consonant in any Given Word
"""
vowel =['a','e','i','o','u']
word = input("Enter the word:").lower()
count_v = 0
count_c = 0
for character in word:
    if character in vowel:
        count_v +=1
    else:
        count_c +=1
print(f"For the {word} there are {count_v} vowels ans {count_c} consonants")

