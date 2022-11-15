from math import pi


# pi = 3.141592
# changed to import pi from math 

radius = float(input('enter the radius of the circle:'))
diameter = 2*radius
circumference = 2*pi*radius
area = pi*diameter
print("Diameter of a circle = %.3f" %diameter)
print("Circumference of a circle = %.3f" %circumference)
print("Area of a circle = %.3f" %area)
