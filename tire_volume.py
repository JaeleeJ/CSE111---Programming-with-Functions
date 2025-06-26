# Jaelee Hutchinson
# 01 Prove Milestone: Review Python
import math

# user input
w = int(input('Enter the width of the tire in mm (ex 205): '))
a = int(input('Enter the aspect ration of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

# calculate volume
v = ((math.pi * (w ** 2) * a) * (w * a + (2540 * d))) / 10000000000

# print
print()
print(f'The approximate volume is {v:.2f} liters')
