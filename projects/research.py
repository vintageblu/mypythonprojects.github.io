#python file for a research project, that was on calculating the wind chill index

import math
print("Please enter the wind speed:")
v = float(input())
print("Please enter the temperature in degrees celsius:")
t = int(input())
b = math.sqrt(v)
a = 10 * b
x = a - v + 10.5
y = 33 - t
z = x * y / 23.1
w = 33 - z
print("The wind chill index is: " + str(w) + ".")
