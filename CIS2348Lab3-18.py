#Chris Rubio
#1530668

import math
print("Enter wall height (feet):")
wall_height = int(input())

print("Enter wall width (feet):")
wall_width = int(input())

wall_area = wall_height * wall_width
print("Wall area:", wall_area, "square feet")

paint = float(wall_area / 350)
print("Paint needed:", "{:.2f}".format(paint), "gallons")

cans = math.ceil(paint)
print("Cans needed:", cans, "can(s)")
print("")
colors = {'red': 35, 'blue': 25, 'green': 23}
print("Choose a color to paint the wall:")
color = input()
print("Cost of purchasing", color, "paint: $"+str(cans*colors[color]))
