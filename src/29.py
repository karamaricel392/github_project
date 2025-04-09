import math

def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

radius = 5  # replace with your own radius value
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")
