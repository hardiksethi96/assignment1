import math
print("The values of sines and cosines from 0" + chr(176) + " to " + "345" + chr(176))
angle = 0
for angle in range(0, 360, 15):
    valuesin = round(math.sin(math.radians(angle)), 4)
    valuecos = round(math.cos(math.radians(angle)), 4)
    print("sin " + str(angle) + chr(176) + " = " + str(valuesin) + "       " + "cos " + str(angle) + chr(176) + " = " + str(valuecos))
