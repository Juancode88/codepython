"""
Write a program that uses 
two dice and the program should
calculate the sum between both values
of the dice also indicates whether the
the value of the result is even or odd
"""
import random 

dice_1 = [1,2,3,4,5,6]
dice_2 = [1,2,3,4,5,6]
random_1 = random.choice(dice_1)
random_2 = random.choice(dice_2)
sum = random_1 + random_2
print(f"dice_1 is: {random_1} and dice 2: {random_2}")
if sum % 2 == 0:
    print(f"The sum is:{sum} this number is even")
else:
    print(f"The sum is:{sum} this number is odd")
