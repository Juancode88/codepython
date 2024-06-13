"""
Python program that converts any unit of length to meters.
"""
conversion_to_meters ={
    'meter':1.0,
    'kilometer':1000.0,
    'centimeter':0.01,
    'foot':0.3048,
}
value = float(input("Enter the value to convert:"))
from_unit = input("Enter the unit to convert from:").lower()
if from_unit not in conversion_to_meters:
    print("ValueError")
else:
    value_in_meters = value * conversion_to_meters[from_unit]
    print(f"{value}{from_unit}(s) is equal to {value_in_meters:.2f} meter(s)")

