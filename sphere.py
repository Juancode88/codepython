"""
Program calculate the area and volume of a sphere
"""
import math
def sphere(radius):
    area = 4 *math.pi * radius **2
    volume = (4/3)* math.pi * radius**3
    return area, volume
a,v = sphere(float(input("Enter the radius:")))
print(f"Area:{a:.3f}")
print(f"volume:{v:.3f}")