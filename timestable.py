"""
generate the times table for any number 
"""
print("Enter the number:")
number =int(input())
for number_2 in range(1,11):
    print(f"{number}X{number_2} = {number*number_2}")
