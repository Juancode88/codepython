"""
Write a program that calculate and return 
a polygon area. The program should receive 
only one polygon for each return and this 
program calculates the area of a square,
triangle and rectangle.
"""
print("Polygon choices: 1.Square 2.Triangle 3.Rectangle")
s=int(input("What is the polygon?:"))
def calculate_p(s):
    if(s == 1):
        side_1 = float(input("How long is side 1 in cm?:"))
        side_2= float(input("How long is side 2 in cm?:"))
        area = side_1*side_2
        print(f"The square area is:{area:.3f}")
    elif(s == 2):
        base = float(input("How long is base in cm?:"))
        height = float(input("How long is height in cm?:"))
        area = (base*height)/2
        print(f"The triangle area is:{area:.3f}")
    elif(s == 3):
        base = float(input("How long is base in cm?:"))
        height = float(input("How long is height in cm?:"))
        area = base*height
        print(f"The Rectangle area is:{area:.3f}")
    else:
        print("ValueError")
    return area
calculate_p(s)
